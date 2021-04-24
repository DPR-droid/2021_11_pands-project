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
import sys

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
userlist = []


# Input data from user
sepallength = float(input("Enter sepal.length between 4.3 to 7.9: "))
userlist.append(sepallength)
sepalwidth = float(input("Enter sepal.width between 2.0 to 4.4: "))
userlist.append(sepalwidth)
petallength = float(input("Enter petal.length between 1.0 to 6.9: "))
userlist.append(petallength)
petalwidth = float(input("Enter petal.width between 0.1 to 2.5: "))
userlist.append(petalwidth)

X_new = np.array([userlist])

prediction = knn.predict(X_new)
arr = (iris['target_names'][prediction])

for i in arr:
    print("The Machine learning model has predcited the iris species as " + i, end = ' ')


