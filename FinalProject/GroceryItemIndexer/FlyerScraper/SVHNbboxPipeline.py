import h5py
import os
import numpy as np
import pandas as pd
from tqdm import tqdm
from datAug import *


def properYOLOFormat(bbox,info=False):
    """
    yolo format
    (x,y) being the center 
    <object-class> <x> <y> <width> <height>
    whatever the author of this ds was smoking
    <height> <y(left)> <x(topleft)> <width> <object-class>
    """
    df = pd.DataFrame(bbox)
    #creating an empty array
    deptArray = len(bbox['height'])
    packer = np.empty([deptArray, 5])
    # <object-class>
    packer[:,0:1:] = np.array(df['label']).reshape((deptArray, 1))
    # <x center>
    packer[:,1:2:] = np.array((df['left'] + (df['width'] / 2))).reshape((deptArray, 1))
    # <y center>
    packer[:,2:3:] = np.array((df['top'] + (df['height'] / 2))).reshape((deptArray, 1))
    # <width>
    packer[:,3:4:] = np.array(df['width']).reshape((deptArray, 1))
    # <height>
    packer[:,4:5:] = np.array(df['height']).reshape((deptArray, 1))
    if info:
        print(f'data before:\n {df}\n')
        print(f'data after <object-class>\t<x>\t<y>\t<width>\t<height>(downScaled):\n{packer}')
    return packer

def get_img_boxes(f, idx=0):
    """
    get the 'height', 'left', 'top', 'width', 'label' of bounding boxes of an image
    :param f: h5py.File
    :param idx: index of the image
    :return: dictionary
    """
    bbox_prop = ['height', 'left', 'top', 'width', 'label']
    meta = { key : [] for key in bbox_prop}

    box = f[bboxs[idx][0]]
    for key in box.keys():
        if box[key].shape[0] == 1:
            meta[key].append(int(box[key][0][0]))
        else:
            for i in range(box[key].shape[0]):
                meta[key].append(int(f[box[key][i][0]][()].item()))

    return meta
    
def get_img_name(f, idx=0):
    img_name = ''.join(map(chr, f[names[idx][0]][()].flatten()))
    return(img_name)

def txtNameFromJPG(jpgName):
    return jpgName.split('.')[0]+'.txt'

urldb = '/home/henri/Downloads/test/'
labelurl = '/home/henri/Downloads/matlab/digitStructTest.mat'
# loading all image files names
onlyfiles = [f for f in listdir(urldb) if isfile(join(urldb, f))]
sortedImg = sorted(onlyfiles)
# loading the label file
digit_file = os.path.join(labelurl)
f = h5py.File(digit_file, 'r')
# since the label file is written in h5 f
names = f['digitStruct/name']
bboxs = f['digitStruct/bbox']

for idx in tqdm(range(len(sortedImg))):
    print(f'working on {sortedImg[idx]}')
    # std the format to yolo
    VHNSToYOLO = properYOLOFormat(get_img_boxes(f, idx),info=False)
    # loading image so that we can asses its width and height
    currentImg = loadImgToArray(urldb+get_img_name(f, idx))
    # create the file
    saveBBox(urldb+txtNameFromJPG(get_img_name(f, idx)),VHNSToYOLO,currentImg,info=False,mode='yolo')

