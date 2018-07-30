For our data set we chose CIFAR-10 a 60,000 32x32 color images divided equally in to ten categorizes. The data set is further divided into 50,000 train and 10,000 test images. The data set can be found at [CS Toronto](https://www.cs.toronto.edu/~kriz/cifar.html) website. Below is a small sample of the images in the data set. 

![](https://github.com/Saltzguy/Lab4/blob/master/Part4/Images/Samples.png) 

For the CNN, I used the code provided by our instructors with some minor modifications. In addition, I used some code to manage the CIFAR-10 data set. I got the code from "Learning TensorFlow A guide to build Deep Learning Systems" by Tom Hope, Yehezkel S. Resheff, and Itay Lider and can be found in the file cifar.py.  
I tried numerous changes to the hyper parameters. Those included three different optimizers, the learning rates, filter sizes, batch sizes, and the number of iterations. Below is the basic graph of the CNN.

![](https://github.com/Saltzguy/Lab4/blob/master/Part4/Images/Graph.png)

The best I was able to get was 65.87% percent with the Adam optimizer, the learning rate set to .001, batch size 100, 10,000 iterations, and the filters set to 16,32,64. Below is the accuracy and loss graph for the best run on the training data. 

![](https://github.com/Saltzguy/Lab4/blob/master/Part4/Images/acc.png)

![](https://github.com/Saltzguy/Lab4/blob/master/Part4/Images/Loss.png)

With the other optimizers, despite all of the changes I made to the hyper parameters, I never was able to get above 60%.

### Conclusion 
With this CNN the best optimizer is Adam. In addition you will want to reduce the filter size and increase the batch size and the number of iterations. But to get a program that can be used in the real world you will need a better CNN.

To view a quick summary of all of the changes I made see Notes.txt. To view all of the data open the runs folder with Tensorboard.