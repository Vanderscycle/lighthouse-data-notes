from datAug import *
from math import sqrt
import argparse

#mainUrl = '/home/henri/Documents/Lighthouse-lab/Databases/final project db/flyerScrapedData/roboflow(test)/'
#AnnotedUrl = '/home/henri/Documents/Lighthouse-lab/Databases/final project db/flyerScrapedData/roboflow Preds(73p)/'
#testUrl = '/home/henri/Documents/Lighthouse-lab/Databases/final project db/flyerScrapedData/predsResults/'

def whatIsIT(classBox):
    labelTranslator = {0: 'Merchandise',1:'price'}
    return labelTranslator[int(classBox)]


def descriptionCropper(mainUrl,directory):
  
    results = dict()
    
    imageArray = loadImgToArray(mainUrl + directory[0], info=False)
    test = loadingBBox(mainUrl + directory[1],imageArray,info=False)

    for i in range(len(test[:,1::])):
        firstBox = test[:,1::][i]
        classBox = whatIsIT(test[:,0:1:][i])
        testImg = imageArray[int(firstBox[1]):int(firstBox[3]) , int(firstBox[0]):int(firstBox[2]),:]
        if  classBox=='Merchandise':
            print('Saved')
            results[i] = [test[i],testImg]
    reindexDict = {i: v for i, v in enumerate(results.values())}
    return reindexDict

def cropAnnottatedPredImages():
    mainUrl,AnnotedUrl,testUrl = opt.loadPred, opt.loadAnn, opt.save 
    directoryimgsDB = directoryImgTxtload(mainUrl,info=False)
    for idx,directoryImg in enumerate(directoryimgsDB):


        croppedAnnotions = descriptionCropper(mainUrl,directoryImg)
        columns = round(sqrt(len(croppedAnnotions))) + 1
        rows = round(sqrt(len(croppedAnnotions))) 

        print(f'number of items {len(croppedAnnotions)}')
        for i in range(1, columns*rows +1):

            if i< len(croppedAnnotions):
                img = croppedAnnotions[i][1]
                
                #fig.add_subplot(rows, columns, i)
                #plt.imshow(img)
                saveArrayToImg(f'{testUrl}Image_{idx}_crop_{i}_results.jpeg',img,info=True)
            else:
                pass
#plt.show()

# cli commands inspired by yolo
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--loadPred', nargs='+', type=str, default='/home/henri/Documents/Lighthouse-lab/Databases/final project db/flyerScrapedData/roboflow(test)/', help='dir path where the .txt and .jpg are located')
    parser.add_argument('--loadAnn', nargs='+', type=str, default='/home/henri/Documents/Lighthouse-lab/Databases/final project db/flyerScrapedData/roboflow Preds(73p)/', help='dir path where the .txt and .jpg are located')
    parser.add_argument('--save', nargs='+', type=str, default="/home/henri/Documents/Lighthouse-lab/Databases/final project db/MNIST-Spicy/groceryPred/", help='dir path where you will save each crop')
    opt = parser.parse_args()
    print(opt)
    cropAnnottatedPredImages()
#python NN1PredPipeline.py 