from datAug import *
from math import floor,ceil
from shutil import copy2
from os import mkdir
import pandas as pd
import argparse

def assignData(directory,size,info=True):
    """
    split comes as a list [8,1,1] [train,val,test]. We round down using floor.
    This method should work well with thousands of sample but for large we will have to explore numpy arrays.
    """
    directory = np.array(directory)
    # error checking
    if len(size)!=3:
        print(f'Requires a list with 3 arguments [train,val,test] you passed {size}')
        return
    # numbers do not tally to a 100
    if sum(size)!=10:
        print(f'Sum of all ints in the list must be 10. You passed {size} and its sum is {sum(size)}')
        return
    train, validate, test = np.split(directory, [int(len(directory)*size[0]/10), int(len(directory)*(sum(size) - size[2])/10)])
    if info:
        [print(i,'\n') for i in [train, validate, test]]
    return train, validate, test

def urlFormater(url,dataset,destName='',mode='dest',info=False):
    """
    mode = [dest,source]
    dataset must be a numpy array
    type is the name of the folder
    """
    dataset = pd.DataFrame(dataset)
    if mode == 'dest':
        # images 
        dataset[0] = url + destName + '/images/' + dataset[0]
        # labels 
        dataset[1] = url + destName + '/labels/' + dataset[1]
        #dataset[:,1:2] = np.char.add(destName,dataset[:,1:2])
    elif mode == 'source':
        dataset = url + dataset
    else:
        print(f'please ensure mode parameters are [dest,source]')
        return    
    if info:
        np.array(dataset)
    # copy2('/src/dir/file.ext', '/dst/dir/newname.ext')
    return np.array(dataset)

def folderSubFolderCreator(destUrl,folder,subfolder):
    """
    Can only do 2 deep at the moment. Mkdir can only create directory one depth at a time
    """
    for f in folder:
        mkdir(destUrl + f'/{f}/')
        for subf in subfolder:
            stringList = [f,subf]
            mkdir(destUrl + '/'.join(string for string in stringList)+'/')

def moveplacenameholder(urlSrc,urlDest,dataset,directory,info=False):
    """
    Of note we will want to shuffle the data eventually. I am unsure if shuffling at the directory will alleviatee headaches
    """
    # orgin
    directory = urlFormater(urlSrc,directory,mode='source')
    subFolder = ['train','valid','test']
    # destination
    tr,vl,ts = [urlFormater(urlDest,d,destName=f,mode='dest') for d,f in zip(dataset,subFolder)]
    #create directories
    folderSubFolderCreator(urlDest,['train','valid','test'],['images','labels'])
    destination = np.concatenate((tr,vl,ts), axis=0)

    for fromImgTxt, toImgTxt in zip(directory, destination):
        print(f'{fromImgTxt}{toImgTxt}')

        for src, dest in zip(fromImgTxt,toImgTxt):
            if info:
                print(src,'/'.join(dest.split('/')[:-1]))
            copy2(src,'/'.join(dest.split('/')[:-1]))


    return

def trainValTest():
    """
    made for yolov5
    
    """
    fromUrl,destUrl,trainValTest = opt.load, opt.save, opt.train_val_test
    print('creating Train Val Test folder at {destUrl} with a split of: {trainValTest} from the images/labels {fromUrl}')
    directory = directoryImgTxtload(fromUrl,info=False)
    tr,va,te = assignData(directory,trainValTest)
    moveplacenameholder(fromUrl,destUrl,[tr,va,te],directory,info=True)
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--load', nargs='+', type=str, default='/home/henri/Desktop/roboflow/224.ext/', help='dir path where the .txt and .jpg are located')
    parser.add_argument('--save', nargs='+', type=str, default='/home/henri/Desktop/roboflow/224.ext/destfolder/', help='main directory where the img and files will be splitted')
    parser.add_argument('--train-val-test',nargs='+', type=list, default=[8,1,1], help='where the train val test split will be determined')
    opt = parser.parse_args()
    print(opt)
    trainValTest()