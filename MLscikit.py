########################################################################
# GMIT project for Programming and Scripting Module
# pands-project
# MLscikit.py
# Author David
##########################################################################

########################################################################
### imports
#######################################################################
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

########################################################################
### sklearn.datasets load_iris 
#######################################################################
iris=load_iris()

########################################################################
### outputs details on the loaded sklearn.datasets load_iris
### to determine changes required for dataframe
#######################################################################
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

########################################################################
### Create the Dataframe in pandas
### sets the target (isis species to an integer)
#######################################################################
data1 = pd.DataFrame(data= np.c_[iris['data'], iris['target']],columns= iris['feature_names'] + ['target'])
data1['target']=pd.to_numeric(data1['target'],downcast='integer')

########################################################################
### Output data 
### sets the target (isis species to an integer)
#######################################################################

print(data1)

########################################################################
# Create training and testing data
#
########################################################################

X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'], random_state = 0)

########################################################################
# output how much is in the training and how much is in the testing data
#
########################################################################

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


########################################################################
# Test the model with dimensions to get output of iris species
# 6.9, 2.9, 4, 1.5
########################################################################
X_new = np.array([[6.9, 2.9, 4, 1.5]])
print(X_new.shape)

print("*******************************")
prediction = knn.predict(X_new)
print(prediction)
print("*******************************")
print(iris['target_names'][prediction])