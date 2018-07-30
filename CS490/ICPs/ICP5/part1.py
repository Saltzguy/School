#%%
import numpy as np 
import matplotlib.pyplot as plt

#just the data
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

#finds the mean of the array
x_mean = np.mean(x)
y_mean = np.mean(y)

# Used to find an estimate of the slope
num = np.sum((x - x_mean)*(y - y_mean))
dem = np.sum(np.power(x - x_mean,2))

slope = num/dem
# intercept of the line
intercept = y_mean - (slope * x_mean)
#formula for the line
result = (slope * x) + intercept

#puts the data on the plot
plt.scatter(x,y)
#Sets the line color to red and puts in on the plot
plt.plot(x,result, color="red")
plt.show()