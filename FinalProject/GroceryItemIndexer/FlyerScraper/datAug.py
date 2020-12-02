import numpy as np
from PIL import Image
from io import StringIO
import copy
from tqdm import tqdm
# plotting libraries 
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
#importing files libraries
from os import listdir
from os.path import isfile, join
# imgaug libraries
import imgaug as ia
import imgaug.augmenters as iaa
from imgaug.augmentables.bbs import BoundingBox, BoundingBoxesOnImage
# img loading/saving and formatting function
def loadImgToArray(url,info=False):
    """
    take the url and return the image (PIL format) as a numpy Array
    """
    with Image.open(url) as image:
    #image = Image.open(url)
        imgArray = np.asarray(image)
    if info:
        print(f'From: {type(image)}, Size: {image.size}, Mode: {image.mode}\nTo: {type(imgArray)}, shape: {imgArray.shape}')
    
    return imgArray

def saveArrayToImg(url,npArray,info=False):
    """
    Takes a numpy array and converts it 
    """
    image = Image.fromarray(npArray)
    if info:
        print(f'From: {type(npArray)}, shape: {npArray.shape}\nTo: {type(image)}, Size: {image.size}, Mode: {image.mode}')
        
    image.save(url)
    image.close()

# box loading/saving and formatting function
def loadingBBox(fileurl,imageArray,info=True,mode='default'):
    """
    Of not if you select the yolo mode you will not be able to use image augmentation
    mode = ['default','yolo']
    Assuming the data is in this format (yolo)
    <object-class> <x> <y> <width> <height> 
    [1.      , 0.250126, 0.29366 , 0.471062, 0.410735]
    the fucntion will return the following format
    <object-class> <x1> <y1> <x2> <y2>

    The following code allowed to push through
    https://github.com/dnissimi/imgaug-yolov3/blob/master/imgaug-yolov3.py
    """
    # width/height of the orginal image
    width = imageArray.shape[1] #width or x axis
    height = imageArray.shape[0] #height of y axis
    boxData = np.loadtxt(fileurl)
    # we want to load the box data but keep the format
    if mode == 'yolo':
        
        boxData[:,1:2:] = boxData[:,1:2:] * width
        boxData[:,2:3:] = boxData[:,2:3:] * height
        boxData[:,3:4:] = boxData[:,3:4:] * width 
        boxData[:,4:5:] = boxData[:,4:5:] * height
        if info:
            print(f'using the {mode} mode. The data is kept in yolo format but scaled') 
            print(f'before transform\n<object-class>\t<x>\t<y>\t<width>\t<height> (unscaled):\n{np.loadtxt(fileurl)}\nafter transform\n<object-class>\t<x>\t<y>\t<width>\t<height> (scaled):\n{boxData}')
        return boxData
    # we want to load the box data in the <object-class> <x1> <y1> <x2> <y2> format
    x1 = boxData[:,1:2:] * width - (boxData[:,3:4:] * width / 2)
    y1 = boxData[:,2:3:] * height - (boxData[:,4:5:] * height / 2)
    x2 = boxData[:,3:4:] * width + x1
    y2 = boxData[:,4:5:] * height + y1
    scaledtransformed = np.column_stack([boxData[:,0:1:],x1,y1,x2,y2])
    if info:
        print(f'using the {mode} mode so the data is converted')
        print(f'\nimage width: {width} and height {height}')
        print(f'before transform\n<object-class>\t<x>\t<y>\t<width>\t<height>:\n{boxData}\n after transform\n<object-class>\t<x1>\t<y1>\t<x2>\t<y2>:\n{scaledtransformed}')

    return scaledtransformed

def saveBBox(fileurl,boxData,imageArray,info=True,mode='default'):
    """
    mode = ['default','yolo']
    Assuming the data is in this format (yolo)
    <object-class> <x1> <y1> <x2> <y2> 
    the fucntion will return the following format
    <object-class> <x> <y> <width> <height>

    Doesn't take into account boxes that fell outside the image size post transformation
    """
    # width/height of the transfomer image
    width = imageArray.shape[1] #width or x axis
    height = imageArray.shape[0] #height of y axis
    # converting from <object-class> <x1> <y1> <x2> <y2>
    if mode == 'default':

        x_pos = boxData[:,1:2:] / width - (( boxData[:,1:2:] - boxData[:,3:4:]) / width / 2)
        y_pos = boxData[:,2:3:] / height - ((boxData[:,2:3:] - boxData[:,4:5:]) / height /2)
        # the original repo had an error there
        x_size = (boxData[:,3:4:] - boxData[:,1:2:]) / width 
        y_size = (boxData[:,4:5:] - boxData[:,2:3:]) / height
        scaledtransformed  = np.column_stack([boxData[:,0:1:],x_pos,y_pos,x_size,y_size])

        # normally we 
        if info:
            print(f'\nimage width: {width} and height {height}')
            print(f'before transform\n<object-class>\t<x1>\t<y1>\t<x2>\t<y2>:\n{boxData} after transform <object-class>\t<x>\t<y>\t<width>\t<height>:\n{scaledtransformed}')
        
        np.savetxt(fileurl, scaledtransformed,fmt='%f', delimiter=' ')

    # need to check that it is wroking
    elif mode == 'yolo':
        # new variable assignement for info message. 
        # Has to do deep copy because later cahnges will overwrite the referenced variable
        before = copy.deepcopy(boxData)
        # downscaling of the data
        boxData[:,1:2:] = boxData[:,1:2:] / width
        boxData[:,2:3:] = boxData[:,2:3:] / height
        boxData[:,3:4:] = boxData[:,3:4:] / width 
        boxData[:,4:5:] = boxData[:,4:5:] / height

        if info:
            print(f'\nimage width: {width} and height {height}')
            print(f'before transform\n<object-class>\t<x>\t<y>\t<width>\t<height>\n{before}\n after transform <object-class>\t<x>\t<y>\t<width>\t<height>:\n{boxData}')
        
        np.savetxt(fileurl, boxData,fmt='%f', delimiter=' ')

    else:
        print('error saving')

def showImg(imgArray):
    """
    takes a numpy array and display as a picture
    """  
    imgplot = plt.imshow(imgArray)
    plt.show()

#box type to numpy type
def bboxNPPacker(bbox):
    """
    bridge the functional gap in converting bbox types of imgaug
    to numpy arrays
    """
    packer = np.empty([len(bbox.bounding_boxes), 5])
    for idx in range(len(bbox.bounding_boxes)):
        bboxIdx = bbox.bounding_boxes[idx]
        packer[idx] = [bboxIdx.label,bboxIdx.x1,bboxIdx.y1,bboxIdx.x2,bboxIdx.y2]
    return packer

def augmentedCopiesSingleImage(imgArray,bbox,amount,info=False):
    results = dict()
    for i in range(0,amount):
        results[i] = seq(image=imgArray, bounding_boxes=bbox)
    return results

def directoryImgTxtload(mainUrl,info=False):
    """
    function that takes the directory link and package jpg and txt files into a list.
    Check for mismatch
    help from: https://stackoverflow.com/questions/21752610/iterate-every-2-elements-from-list-at-a-time
    """
    
    onlyfiles = [f for f in listdir(mainUrl) if isfile(join(mainUrl, f))]
    sortedImgTxt = sorted(onlyfiles)
    # return sortedImgTxt
    # #it = iter(sortedImgTxt)
    combinedList = list()
    # # the only things that should be in the folder should be (jpg/) and txt
    for i, v in  zip(sortedImgTxt[0::2], sortedImgTxt[1::2]):
        if info:
            print(i, v)
        combinedList.append(list([i,v]))
    
        #check for mismatch of files
        if (i.split('.')[0]) != (v.split('.')[0]):
            print(f'Mismatched file detected {[i,v]} in directory {mainUrl} purging results.\nUser please take action!')
            combinedList = list()
            break
    return combinedList

def fileNameAugGen(i,fileName):
    """
    Handles the rename and indexing of the file
    """
    oldJpgName = fileName[0].split('.')
    oldTxtName = fileName[1].split('.')
    newName = [oldJpgName[0] +f'aug{i}.' + oldJpgName[1],oldTxtName[0] +f'aug{i}.' + oldTxtName[1]]
    return newName

#setting the imgaug library
# it would good to move this in a function and have an option to make it spicy
sometimes = lambda aug: iaa.Sometimes(0.5, aug)
seq = iaa.Sequential([

# the most important part of the image transformation

    sometimes(iaa.CropAndPad(
            percent=(-0.05, 0.2),
            pad_mode=ia.ALL,
            pad_cval=(0, 255)
        )),
    sometimes(iaa.Affine(
            scale={"x": (0.8, 1.2), "y": (0.8, 1.2)}, # scale images to 80-120% of their size, individually per axis
            translate_percent={"x": (-0.2, 0.2), "y": (-0.2, 0.2)}, # translate by -20 to +20 percent (per axis)
            rotate=(-45, 45), # rotate by -45 to +45 degrees
            shear=(-16, 16), # shear by -16 to +16 degrees
            order=[0, 1], # use nearest neighbour or bilinear interpolation (fast)
            cval=(0, 255), # if mode is constant, use a cval between 0 and 255
            mode=ia.ALL # use any of scikit-image's warping modes (see 2nd image from the top for examples)
        ))

# everything bellow is nice but not required as it greatly affect the img visibility
# for more info check the github repo

        # iaa.SomeOf((0, 5),
        #     [
        #         #sometimes(iaa.Superpixels(p_replace=(0, 1.0), n_segments=(20, 200))), # convert images into their superpixel representation
        #         iaa.OneOf([
        #             iaa.GaussianBlur((0, 3.0)), # blur images with a sigma between 0 and 3.0
        #             iaa.AverageBlur(k=(2, 7)), # blur image using local means with kernel sizes between 2 and 7
        #             iaa.MedianBlur(k=(3, 11)), # blur image using local medians with kernel sizes between 2 and 7
        #         ]),
        #         iaa.Sharpen(alpha=(0, 1.0), lightness=(0.75, 1.5)), # sharpen images
        #         iaa.Emboss(alpha=(0, 1.0), strength=(0, 2.0)), # emboss images
        #         # search either for all edges or for directed edges,
        #         # blend the result with the original image using a blobby mask
        #         iaa.SimplexNoiseAlpha(iaa.OneOf([
        #             iaa.EdgeDetect(alpha=(0.5, 1.0)),
        #             iaa.DirectedEdgeDetect(alpha=(0.5, 1.0), direction=(0.0, 1.0)),
        #         ])),
        #         iaa.AdditiveGaussianNoise(loc=0, scale=(0.0, 0.05*255), per_channel=0.5), # add gaussian noise to images
        #         iaa.OneOf([
        #             iaa.Dropout((0.01, 0.1), per_channel=0.5), # randomly remove up to 10% of the pixels
        #             iaa.CoarseDropout((0.03, 0.15), size_percent=(0.02, 0.05), per_channel=0.2),
        #         ]),
        #         iaa.Invert(0.05, per_channel=True), # invert color channels
        #         iaa.Add((-10, 10), per_channel=0.5), # change brightness of images (by -10 to 10 of original value)
        #         iaa.AddToHueAndSaturation((-20, 20)), # change hue and saturation
        #         # either change the brightness of the whole image (sometimes
        #         # per channel) or change the brightness of subareas
        #         iaa.OneOf([
        #             iaa.Multiply((0.5, 1.5), per_channel=0.5),
        #             iaa.FrequencyNoiseAlpha(
        #                 exponent=(-4, 0),
        #                 first=iaa.Multiply((0.5, 1.5), per_channel=True),
        #                 second=iaa.LinearContrast((0.5, 2.0))
        #             )
        #         ]),
        #         iaa.LinearContrast((0.5, 2.0), per_channel=0.5), # improve or worsen the contrast
        #         iaa.Grayscale(alpha=(0.0, 1.0)),
        #         sometimes(iaa.ElasticTransformation(alpha=(0.5, 3.5), sigma=0.25)), # move pixels locally around (with random strengths)
        #         sometimes(iaa.PiecewiseAffine(scale=(0.01, 0.05))), # sometimes move parts of the image around
        #         sometimes(iaa.PerspectiveTransform(scale=(0.01, 0.1)))
        #     ],
        #     random_order=True)
])
mainUrl = '/home/henri/Desktop/roboflow/'
testUrl = '/home/henri/Desktop/roboflow/quickTest/'