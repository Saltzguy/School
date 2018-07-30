#%%
from datetime import datetime
import random as rand
import matplotlib.pyplot as plt 
import numpy as np 

from sklearn.cluster import KMeans

def gen_array(low_height: int, high_height: int, low_weight: int, high_weight: int, sample :int):
    #random seed for the data
    rand.seed(datetime.now())
    data = []
    for _ in range(0,sample):
        #need a better distrobution to simulate height
        height= rand.uniform(low_height,high_height)
        chest = rand.uniform(low_weight,high_weight)
        data.append([height,chest])
       
    #returns an narray
    return np.asarray(data)


#generates the random data
#55 inches to 84inches 75 lbs to 300lbs 100 samples
X = gen_array(55,84,75,300,100)
print(X)

#sets the number of clusters
kmeans= KMeans(n_clusters=3)
#Compute cluster centers and predict cluster index for each sample.
kmeans.fit(X)
#finds the label data
y_kmeans = kmeans.predict(X)

plt.scatter(X[:, 0], X[:, 1], c=y_kmeans)
#finds the clusters
centers = kmeans.cluster_centers_
#labels the center clusters black and sets the size to 20
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=20);
plt.show()
