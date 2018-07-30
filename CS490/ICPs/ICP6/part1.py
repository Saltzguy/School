#%%
import numpy as np
from sklearn.cross_validation import train_test_split, cross_val_score
from sklearn.datasets import load_iris
from sklearn.naive_bayes import GaussianNB

gnb = GaussianNB()
data = load_iris()

#pulls the iris feature array from data
iris_x = data.data
#pulls the iris label array from the data
iris_y = data.target

#splits the data to 70/30
x_train, x_test, y_train, y_test = train_test_split(iris_x,iris_y, test_size=0.3)
gnb.fit(x_train,y_train)

score = cross_val_score(gnb, x_test, y_test, cv=10)
#compare the scores using cross val GaussianNB.socre
print(gnb.score(x_test,y_test))
print(np.mean(score))