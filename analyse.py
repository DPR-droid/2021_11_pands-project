########################################################################
# GMIT project for Programming and Scripting Module
# pands-project
# analyse.py
# Author David
########################################################################

########################################################################
# Program updated 20/04/2021
########################################################################

########################################################################
### import pandas module
########################################################################
import pandas as pd
import os.path
from os import path

#fileexists = False
fileexists = path.exists("iris.data")
########################################################################
### Simple file check
########################################################################
if (fileexists == False):
    print("The file does not exist") 
    exit()
else:
    print("The file exists") 

########################################################################
### Read data file and add headers
########################################################################
dataset = pd.read_csv("iris.data",header=None, names=["sepal.length","sepal.width","petal.length","petal.width","species"])

########################################################################
# output a descriptive analysis of the Dataset and Species
# count() 	    Number of non-null observations
# mean() 	    Mean of Values
# std() 	    Standard Deviation of the Values
# min() 	    Minimum Value
# 25%/50%/75%   Percentiles
# max() 	    Maximum Value
########################################################################

print(dataset.describe())

# Group by Species
gk = dataset.groupby('species')

print("Setosa")
# Display the means of the Iris-setosa
print(gk.get_group('Iris-setosa').describe())

print("versicolor")
# Display the means of the Iris-versicolor
print(gk.get_group('Iris-versicolor').describe())

print("virginica")
# Display the means of the Iris-versicolor
print(gk.get_group('Iris-virginica').describe())



