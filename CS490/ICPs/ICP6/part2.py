#%%
import pandas
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#returns the sample stock data as a data frame
stocks_df = pandas.read_csv("sample_stocks.csv")

#creates the kmeasns clutering and sets the number of clusters
#could uses elbow method
kmeans = KMeans(n_clusters=3)
#finds the center of the clusters
kmeans.fit(stocks_df)

#returns the predicted group for the stock data
y_kmeans = kmeans.predict(stocks_df)
#gets cluster centers
centers = kmeans.cluster_centers_

#display the results
plt.scatter(stocks_df.returns, stocks_df.dividendyield, c = y_kmeans)
plt.scatter(centers[:, 0], centers[:, 1], c='green', s=30)
plt.xlabel("returns")
plt.ylabel("dividend yield")
plt.show()

