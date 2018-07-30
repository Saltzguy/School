

### TensorBoard Graph 
![](https://github.com/Saltzguy/Lab3/blob/master/Part1/Images/TensorBoard.png)

***

### Comparison of optimizers from Epoch 0 to 50

**Gradient Descent Optimizer**
![](https://github.com/Saltzguy/Lab3/blob/master/Part1/Images/GradientDescentOptimizer.png)

**RMSProp Optimizer**
![](https://github.com/Saltzguy/Lab3/blob/master/Part1/Images/RMSPropOptimizer.png)

**Adam Optimizer**
![](https://github.com/Saltzguy/Lab3/blob/master/Part1/Images/AdamOptimizer.png)

**Adagrad Optimizer**
![](https://github.com/Saltzguy/Lab3/blob/master/Part1/Images/AdagradOptimizer.png)

### Conclusion
All optimizers reached roughly the same loss by Epoch 50. Gradient descent and RMSProp reached it much faster than the other two. 
***
### Comparing RMSProp Optimizer at Different Learning Rates
**learning rate = .0001**
![](https://github.com/Saltzguy/Lab3/blob/master/Part1/Images/lr0.0001.png)
**learning rate = .0005**
![](https://github.com/Saltzguy/Lab3/blob/master/Part1/Images/lr0.0005.png)
**learning rate = .001**
![](https://github.com/Saltzguy/Lab3/blob/master/Part1/Images/lr0.001.png)
**learning rate = .005**
![](https://github.com/Saltzguy/Lab3/blob/master/Part1/Images/lr0.005.png)
### Conclusion
The RMSProp Optimizer performed best on this data set when the learning rate was equal to .001.
Which is not surprising as that is the recommend default learning rate.
