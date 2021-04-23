########################################################################
# GMIT project for Programming and Scripting Module
# pands-project
# analyse.py
# Author David
##########################################################################


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

iris=load_iris()

print(iris['DESCR'])
print("*******************************")
print(iris.keys())
print("*******************************")
print(iris['target_names'])
print("*******************************")
print(iris['feature_names'])
print("*******************************")
print(iris['data'].shape)
print("*******************************")
print(iris['data'])
print("*******************************")
data1 = pd.DataFrame(data= np.c_[iris['data'], iris['target']],columns= iris['feature_names'] + ['target'])
data1['target']=pd.to_numeric(data1['target'],downcast='integer')

print(data1)

########################################################################
# Create training data
#
########################################################################

X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'], random_state = 0)

print("*******************************")
print(X_train.shape)
print(X_test.shape)
print("*******************************")

########################################################################
# Create the model and test accuracy of the model
# 
########################################################################


knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train, y_train)

print(knn.score(X_test, y_test))
print("*******************************")






