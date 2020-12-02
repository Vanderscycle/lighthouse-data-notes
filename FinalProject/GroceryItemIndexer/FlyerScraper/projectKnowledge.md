ToC:
* How [yolov3 works](https://blog.paperspace.com/how-to-implement-a-yolo-object-detector-in-pytorch/)
    * yolov3 is the last model Joseph Redmon worked on before finishing.
    * Residual Blocks, skip connections, and Upsampling
    * vanishing/exploding gradient (check Andrew Ng)
    * object detection, bounding box regression, IoU and non-maximum suppression (NNS)
    * we will explain v3 since its the last version that the author worked on 
* differences in [yolov3,v4,v5](https://towardsdatascience.com/yolo-v4-or-yolo-v5-or-pp-yolo-dad8e40f7109)
* Why I chose yolov5
    * ultralytic yolov3 PyTorch implementation allowed me to understand yolo better than C/CUDA.
    * ultralytic github repo is clean and concise which allowed to not get lost.
    * yolov4 darknet implementation [is faster](https://github.com/AlexeyAB/darknet/issues/5920#issuecomment-642812152), but my understanding of Darknet(C+CUDA) is lacking 
* [metrics](https://medium.com/@yanfengliux/the-confusing-metrics-of-ap-and-map-for-object-detection-3113ba0386ef) since they can be confusing af 
* why I chose roboflow ai
    * best features remain dataset version control, easy quality control, label and image management
    * I didn't usee their image augmentation since I augmented my images with imgAug
    * todo: create a py file that split data between train,test,validate
[yolov4 github](https://github.com/AlexeyAB/darknet) by Alexis
* what is COCO (common object in context) a 330k image dataset with 1.5 million object instances in 80 object categories

## Required knowledge
### Resnet and its Residual blocks component
[helpful article](https://towardsdatascience.com/residual-blocks-building-blocks-of-resnet-fd90ca15d6ec)
Why do we want deep neural networks to begin with?
Higher layers count leads to a higher level of features that can be extracted from the source data. This in turns allow neural networks to become deepeer. Residual network get their name from their identity function: 
* R(x) = Output — Input = H(x) — x
* H(x) = R(x) + x
By providing a different path (skip) we provide an alternative path for the gradient (with backpropagation).

Resnet like DenseNet skip connections.

#### Degradation problems of deep (C)NN
Shallower networks are learning better than their deeper counterparts. 

An identity function is a function that always returns the same value that was used as its argument e.g. H(xi) = xi. In neural networks that means an identity matrix. For a single neuron with 2 input defined by: (Y=W1X1+W2X2+b) z will go through our activation function
### Curse of dimensionality
As the number of features grows, the amount of data required to deneralize accurately grows exponentially. The main issues comes that with higher dimensions the distance between each data points (given that the data size hasn't cahnged) will increase. So we will need more data to fill the space created from the higher dimension.

#### Example
In our fruit example we may want one feature handling color, one for weight, one for shape, etc. Each feature adds information, and if we could handle every feature possible we could tell perfectly which fruit we are considering. However, an infinite number of features requires an infinite number of training examples, eliminating the real-world usefulness of our network. 

The first way to mitigate the curse is by:
1. Carefuly selecting the number of dimensions (features) the model will use.
2. For computer vision Residual block seems to help

### vanishing/exploding gradient
Check andrew Ng but 

I think for the gradient issue, you have to remember that the gradient for each layer is basically the inputs of that layer, times what ever the gradient was up to that layer. If you have a sigmoid/tanh activations, you will have that the inputs will always be a fraction. This might not be a big problem for the last layers, but as you back propagate backwards more and  more, always multiplying by a fraction, you get smaller and smaller gradients, which makes it harder and harder for the weights of those layers to learn.
Similarly - if your activation function can takes larger values (say ReLu) - you run the risk of your gradients becoming bigger and bigger ("exploding") as you backpropagate.

### Intersection over Union (IoU)
[tutorial](https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/)
In order to apply Intersection over Union to evaluate a predicted bouding box we neeed:
* The ground-truth bonding boxees (what we hand labelled)
* The predicted bounding boxes of our model

The equation is simple IoU = Area of Overlap (Ground-truth bbox U' predicted bbox) / Area of Union (Ground truth bbox U predicted bbox)

### non-maximum suppression (NNS)
[tutorial](https://www.analyticsvidhya.com/blog/2020/08/selecting-the-right-bounding-box-using-non-max-suppression-with-implementation/)
Yolo can detect multiple objects that really only bellong to the same object. We can discriminate using NMS. The main two consideration are:
* the objectiveness score()
* the IoU

The general idea is as follow:

* Step 1: Select the box with highest objectiveness score
* Step 2: Then, compare the overlap (intersection over union) of this box with other boxes
* Step 3: Remove the bounding boxes with overlap (intersection over union) >50%
* Step 4: Then, mov to the next highest objectiveness score
* Step 5: Finally, repeat steps 2-4

## How YOLOv3 works:
Residual Blocks: due to the vanishing/exploding gradient experienced by deep NN and the curse of dimensionality(number of features or dimensions)

The NN has 75 convolutional layers with skip conneections and upsampling layer
torch.nn.Conv2d elements:
* padding: the number of cells  that are added on the outside of the image
* stride: how muc the kernel matrix moves per iterations. Stride 2 means 2 movements to the right and is a way to downsample an input.
* kernel size: the nxn convolution matrix
* dilation: space between kernel matrix.

Yolo prefers images that are multiples of 32 since there is a stride of 32. which means that an image of size 416x416 will yield 13x13.

Since the image is divided into cells, eeach cells is responsible of detection up to 3 bouding boxes.

attributes o