########################################################################
# GMIT project for Programming and Scripting Module
# pands-project
# analyse.py
# Author David
# This script requires the full git repository to be downloaded.
# https://github.com/DPR-droid/pands-project
########################################################################

########################################################################
# Program updated 24/04/2021 Finalise program analyse.py
########################################################################

########################################################################
# Supress warning associated with notification of a seaborn deprecated 
# function
########################################################################
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

########################################################################
# imports
########################################################################
import pandas as pd
import os.path
from os import path
import matplotlib.pyplot as plt
import seaborn as sns


########################################################################
# Simple file check if user has not download full git repository with 
# the iris.data file
########################################################################
fileexists = path.exists("iris.data")

if (fileexists == False):
    print("The file does not exist please download full git repository") 
    print("https://github.com/DPR-droid/pands-project") 
    exit()
else:
    print("The file exists") 

########################################################################
### Read data file and add headers
########################################################################
dataset = pd.read_csv("iris.data",header=None, names=["sepal.length","sepal.width","petal.length","petal.width","species"])

########################################################################
### Output data to csv text file for Project requirements
########################################################################
dataset.to_csv('fisher_iris.csv')


########################################################################
# Lock dataset for each species
########################################################################
iris_setosa=dataset.loc[dataset["species"]=="Iris-setosa"]
iris_versicolor=dataset.loc[dataset["species"]=="Iris-versicolor"]
iris_virginica=dataset.loc[dataset["species"]=="Iris-virginica"]


########################################################################
# Outputs summary to a single text file for Project requirements
########################################################################
f =  open("OutputSummary.txt", "w")
f.write("########################################################################\n")
f.write("# Output a descriptive analysis of the Iris Dataset\n")
f.write("# count() 	    Number of non-null observations\n")
f.write("# mean() 	    Mean of Values\n")
f.write("# std() 	    Standard Deviation of the Values\n")
f.write("# min() 	    Minimum Value\n")
f.write("# 25%/50%/75%     Percentiles\n")
f.write("# max() 	    Maximum Value\n")
f.write("########################################################################\n")
f.write(str(dataset.describe()))
f.write("\n\n\n########################################################################\n")
f.write("# Output a descriptive analysis of the Iris Setosa\n")
f.write(str(iris_setosa.describe()))
f.write("\n\n\n########################################################################\n")
f.write("# Output a descriptive analysis of the Iris Versicolor\n")
f.write(str(iris_versicolor.describe()))
f.write("\n\n\n########################################################################\n")
f.write("# Output a descriptive analysis of the Iris Virginica\n")
f.write(str(iris_virginica.describe()))
f.close()


########################################################################
# exit for test purposes
########################################################################
exit()
########################################################################
# Histogram of Iris dataset
# UserWarning: The `size` parameter has been renamed to `height`; 
# please update your code.
########################################################################
sns.FacetGrid(dataset,hue="species",height=3).map(sns.distplot,"petal.length").add_legend()
sns.FacetGrid(dataset,hue="species",height=3).map(sns.distplot,"petal.width").add_legend()
sns.FacetGrid(dataset,hue="species",height=3).map(sns.distplot,"sepal.length").add_legend()
sns.FacetGrid(dataset,hue="species",height=3).map(sns.distplot,"sepal.width").add_legend()
# plt.show()


########################################################################
# Create a boxplot
########################################################################
sns.boxplot(x="species",y="petal.length",data=dataset)
# plt.show()


########################################################################
# Create a Pairwise plots/scatterplot matrix
########################################################################
g = sns.PairGrid(dataset, hue="species")
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
g.add_legend()
# plt.show()

########################################################################
# Create a violin plot
#
########################################################################
sns.violinplot(x="species",y="petal.length",data=dataset)
# plt.show()
