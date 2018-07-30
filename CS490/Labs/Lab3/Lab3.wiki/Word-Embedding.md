Part 2 Word Embedding

***
For the data set we chose to use the novel The Golden South by Lambert Kathleen due to it being free from images and markups such as HTML tags. The book can be found at [Project Gutenberg](http://www.gutenberg.org/ebooks/57484). We also used the Word2Vec program provided by the teachers.

***
### TensorBoard Graph
![](https://github.com/Saltzguy/Lab3/blob/master/Part2/images/graph.png)

###  Comparison of Optimizers for 20000 steps
**Adam Optimizer**
![](https://github.com/Saltzguy/Lab3/blob/master/Part2/images/Adam.png)
**Gradient Descent Optimizer**
![](https://github.com/Saltzguy/Lab3/blob/master/Part2/images/Gradient.png)
**RMSProp Optimizer**
![](https://github.com/Saltzguy/Lab3/blob/master/Part2/images/RMSProp.png)
### Conclusion 
The Adam Optimizer produce better results than both the RMSProp and the Gradient Descent. Which surprised me as I though the Adam would produce similar results to the RMSProp due to the Adam Optimizer is based on the RMSProp. Another thing that surprised me was how much faster the Gradient Descent and the RMSProp ran vs the Adam but, with worse results.

***

###  Comparison of Optimizers for 50000 steps

**Adam Optimizer**
![](https://github.com/Saltzguy/Lab3/blob/master/Part2/images/Adam50000.png)
**Gradient Descent Optimizer**
![](https://github.com/Saltzguy/Lab3/blob/master/Part2/images/Gradient50000.png)
**RMSProp Optimizer**
![](https://github.com/Saltzguy/Lab3/blob/master/Part2/images/Rmsp50000.png)
### Conclusion 
Once again, the Adam Optimizer produce better results than the others but, took a far longer time to run. 

***

**Word Plot** 
Note: This is the Adam Optimizer word plot for 20000 steps. If you wish to see the others they are in the images folder
![](https://github.com/Saltzguy/Lab3/blob/master/Part2/images/4thRun.png)

### Conclusion:
The above graph is from the Adam Optimizer using 50000 steps. It appears that some of the words have a meaningful location compared to the other words. One example would be “their” and “are” in the lower left-hand corner. I imagine those two words are used quite often together, which would justify their locations compared to the other. It should be noted, I did find results similar for all optimizers on all runs. 
***

### Ending Remarks
I changed multiple parameters on all the tested optimizer, such as the learning rate, the window size, and embedding size but, I was not able to achieve any noticeable improvements over my initial test. This could due to the size of the data set or the type of the data. If I were to do over this lab, I would use a more popular data set to compare my results with those of other people.