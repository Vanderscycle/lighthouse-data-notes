#vscode will toss you aa warning but that doesn't mean anything as this is the correct way to import everything
# I think the answer is somewhere in the settings path of the file
from datAug import *
import argparse
from tqdm import  tqdm

# mainUrl = '/home/henri/Desktop/roboflow/'
# testUrl = '/home/henri/Desktop/roboflow/224.ext/'
def augmentImages():
    mainUrl,testUrl,lowThresholdRand,highThresholdRand = opt.load, opt.save, opt.low_img_rand, opt.high_img_rand
    directory = directoryImgTxtload(mainUrl)
    for f in tqdm(range(len(directory))):
        
        imageArray = loadImgToArray(mainUrl + directory[f][0], info=False)
        Bdata = loadingBBox(mainUrl + directory[f][1],imageArray,info=False)
        print(f'\nworking on {directory[f][0]} {directory[f][1]}')
        bbs = list()
        for box in Bdata:
            Bclass,x1,y1,x2,y2 = box
            bbs.append(BoundingBox(label=Bclass,x1=x1, y1=y1, x2=x2, y2=y2))
        bbs = BoundingBoxesOnImage(bbs,shape=imageArray.shape)
        # I am running out of memory maybe this will help
        augmentedImagesList = augmentedCopiesSingleImage(imageArray,bbs,np.random.randint(lowThresholdRand,high=highThresholdRand))
        for i in range(len(augmentedImagesList)):
            jpgNewName, txtNewName = fileNameAugGen(i,directory[f])
            saveArrayToImg(testUrl + jpgNewName, augmentedImagesList[i][0],info=False)
            #! error bellow
            #url,
            saveBBox(testUrl + txtNewName, bboxNPPacker(augmentedImagesList[i][1]), augmentedImagesList[i][0], info=False)

# cli commands inspired by yolo
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--load', nargs='+', type=str, default='/home/henri/Desktop/roboflow/', help='dir path where the .txt and .jpg are located')
    parser.add_argument('--save', nargs='+', type=str, default='/home/henri/Desktop/roboflow/224.ext/', help='dir path where the .txt and .jpg are located')
    parser.add_argument('--low-img-rand', type=int, default=2, help='lowest number of sample that are procuded per image')
    parser.add_argument('--high-img-rand', type=int, default=5, help='highest number of sample that are procuded per image')
    opt = parser.parse_args()
    print(opt)
    augmentImages()
# python imageAugmenterPipeline.py 