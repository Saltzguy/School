
Compare the results of CNN and RNN/LSTM models, for the text classification (same dataset for 2 models to compare) and describe, which model is best for the text classification based on your results :

CNN: Conclusion: AdamOptimizer with filter size(3,4,5), number of filter=128, dropout probability= 0.5 batch size=64, number of epochs =100, have the best accuracy(0.826531)

RNN/LSTM: with 10000 iterations, the average loss was 11.035806, and the  average accuracy was 3.80%

There are various designs of the RNN and CNN depends on which dataset we are choosing. According to test result the accuracy and loss of question 1 and question 2, there is a huge difference between both networks. The CNN works better, has a high accuracy and lower loss. In performance comparison between them, whether a CNN is better, depends on the problem. When we were running both models, the RNN seems like a more 'natural' approach, given that text is naturally sequential. However, RNNs are quite slow and fickle to train.
