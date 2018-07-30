For part 2 I used a multi-layer LSTM with 2 layers.
With both data set one and two I varied the learning rate (0.01, 0.001) as well as the n_hidden (512, 1024)
Below is the graph of the RNN.

![](https://github.com/Saltzguy/Lab4/blob/master/Part2/newdata2_graph.png)

### Conclusion
As you will see from the output, I did not receive an accuracy greater than about 7.00%. It's extremely low. This leads me to believe that a LSTM RNN is not the correct choice for predicting this type of data.