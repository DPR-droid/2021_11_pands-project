########################################################################
# GMIT project for Programming and Scripting Module
# pands-project
# analyse.py
# Author David
########################################################################

########################################################################
# Program updated 21/04/2021 ouput plots
########################################################################

########################################################################
### imports
########################################################################
import pandas as pd
import os.path
from os import path
########################################################################
# imports for plots
########################################################################
import matplotlib.pyplot as plt
import seaborn as sns

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
#gk = dataset.groupby('species')

#print("Setosa")
# Display the means of the Iris-setosa
#print(gk.get_group('Iris-setosa'))

#print("versicolor")
# Display the means of the Iris-versicolor
# print(gk.get_group('Iris-versicolor').describe())

#print("virginica")
# Display the means of the Iris-versicolor
# print(gk.get_group('Iris-virginica').describe())


########################################################################
# create each species into a dataset
#
########################################################################

iris_setosa=dataset.loc[dataset["species"]=="Iris-setosa"]
iris_versicolor=dataset.loc[dataset["species"]=="Iris-versicolor"]
iris_virginica=dataset.loc[dataset["species"]=="Iris-virginica"]

########################################################################
# Test group
#
########################################################################

#print(iris_setosa)
#print(iris_versicolor)
#print(iris_virginica)

########################################################################
# Try histogram using seaborn module
#
########################################################################

#sns.FacetGrid(dataset,hue="species",size=3).map(sns.distplot,"petal.length").add_legend()
#sns.FacetGrid(dataset,hue="species",size=3).map(sns.distplot,"petal.width").add_legend()
#sns.FacetGrid(dataset,hue="species",size=3).map(sns.distplot,"sepal.length").add_legend()
#sns.FacetGrid(dataset,hue="species",size=3).map(sns.distplot,"sepal.width").add_legend()
# plt.show()


########################################################################
# Create a boxplot
#
########################################################################

# sns.boxplot(x="species",y="petal.length",data=dataset)
# sns.boxplot(x="species",y="sepal.length",data=dataset)
# sns.boxplot(x="species",y="petal.width",data=dataset)
sns.boxplot(x="species",y="sepal.width",data=dataset)
plt.show()