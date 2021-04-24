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
    print("The iris.data file exists\n") 

########################################################################
### Read data file and add headers
########################################################################
dataset = pd.read_csv("iris.data",header=None, names=["sepal.length","sepal.width","petal.length","petal.width","species"])

########################################################################
### Output data to csv text file for Project requirements
########################################################################
dataset.to_csv('fisher_iris.csv')
print("Output dataset to csv file completed\n")

########################################################################
# Lock dataset for each species
########################################################################
iris_setosa=dataset.loc[dataset["species"]=="Iris-setosa"]
iris_versicolor=dataset.loc[dataset["species"]=="Iris-versicolor"]
iris_virginica=dataset.loc[dataset["species"]=="Iris-virginica"]


########################################################################
# Outputs summary to a single text file for Project requirements
########################################################################
with open("OutputSummary.txt",'w') as f:
    f.write("########################################################################\n")
    f.write("# Output a descriptive analysis of the Iris Dataset\n")
    f.write("# count() 	    Number of non-null observations\n")
    f.write("# mean() 	    Mean of Values\n")
    f.write("# std() 	    Standard Deviation of the Values\n")
    f.write("# min() 	    Minimum Value\n")
    f.write("# 25%/50%/75%      Percentiles\n")
    f.write("# max() 	    Maximum Value\n")
    f.write("########################################################################\n")
    f.write(str(dataset.describe()))
    f.write("\n\n########################################################################\n")
    f.write("# Output a descriptive analysis of the Iris Setosa\n")
    f.write("########################################################################\n")
    f.write(str(iris_setosa.describe()))
    f.write("\n\n########################################################################\n")
    f.write("# Output a descriptive analysis of the Iris Versicolor\n")
    f.write("########################################################################\n")
    f.write(str(iris_versicolor.describe()))
    f.write("\n\n########################################################################\n")
    f.write("# Output a descriptive analysis of the Iris Virginica\n")
    f.write("########################################################################\n")
    f.write(str(iris_virginica.describe()))

print("Output summary data\n")

########################################################################
# Outputs plot to png for Project requirements
########################################################################
########################################################################
# Histogram of Iris dataset
# UserWarning: The `size` parameter has been renamed to `height`; 
# please update your code.
########################################################################
sns.FacetGrid(dataset,hue="species",height=3).map(sns.distplot,"petal.length").add_legend()
plt.savefig('HistPL.png')
sns.FacetGrid(dataset,hue="species",height=3).map(sns.distplot,"petal.width").add_legend()
plt.savefig('HistPW.png')
sns.FacetGrid(dataset,hue="species",height=3).map(sns.distplot,"sepal.length").add_legend()
plt.savefig('HistSL.png')
sns.FacetGrid(dataset,hue="species",height=3).map(sns.distplot,"sepal.width").add_legend()
plt.savefig('HistSW.png')

print("Output of histograms completed\n")

########################################################################
# Create a boxplot
# Overlap in label use xticks to rotate label on the x axis
########################################################################
sns.boxplot(x="species",y="petal.length",data=dataset)
plt.xticks(x="species", rotation='vertical')
plt.savefig('BoxPL.png')

print("Output of boxplot completed\n")

########################################################################
# Create a violin plot
########################################################################
sns.violinplot(x="species",y="petal.length",data=dataset)
plt.savefig('ViolinPL.png')

print("Output of violin plot completed\n")

########################################################################
# Create a Pairwise plots/scatterplot matrix
########################################################################
g = sns.PairGrid(dataset, hue="species")
g.map_diag(sns.histplot)
g.map_offdiag(sns.scatterplot)
g.add_legend()
plt.savefig('Pairwise-Scatterplots.png')

print("Output of Pairwise plots/scatterplot matrix completed\n")


########################################################################
# Test if user has sklearn module is installed
# Installing a module is the users decision
########################################################################
try:
    import sklearn
    print("sklearn module detected commencing Machine Learning\n")
except ImportError as e:
    print("Unfortunately you do not have sklearn modules installed\n")
    print("Please install using the following command\n")
    print("pip install -U scikit-learn")
    print("\n")
    exit()


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

########################################################################
### sklearn.datasets load_iris 
#######################################################################
iris=load_iris()


########################################################################
### Create the Dataframe in pandas
### sets the target (isis species to an integer)
#######################################################################
data1 = pd.DataFrame(data= np.c_[iris['data'], iris['target']],columns= iris['feature_names'] + ['target'])
data1['target']=pd.to_numeric(data1['target'],downcast='integer')

########################################################################
### Update Text file
#######################################################################

########################################################################
### To add numpy.array to textfile
### np.savetxt(f2, speciestype, fmt='%s')
### np.savetxt(f2, dimensionnames, fmt='%s')
#######################################################################
speciestype = iris['target_names']
dimensionnames = iris['feature_names']

with open("OutputSummary.txt",'r') as f:
        with open("newfile.txt",'w') as f2: 
            f2.write("########################################################################\n")
            f2.write("# Decription of the Fisher Iris Database\n")
            f2.write("########################################################################\n")
            f2.write(str(iris['DESCR']))
            f2.write("\n\n########################################################################\n")
            f2.write("# Iris Species Type\n")
            f2.write("########################################################################\n")
            np.savetxt(f2, speciestype, fmt='%s')
            f2.write("\n\n########################################################################\n")
            f2.write("# Feature names\n")
            f2.write("########################################################################\n")
            np.savetxt(f2, dimensionnames, fmt='%s')
            f2.write("\n\n########################################################################\n")
            f2.write("# Database size\n")
            f2.write("########################################################################\n")
            f2.write(str(iris['data'].shape))
            f2.write("\n\n########################################################################\n")
            f2.write("# Database summary\n")
            f2.write("########################################################################\n")
            f2.write(str(data1))
            f2.write("\n\n")
            f2.write(f.read())

########################################################################
### Read old text, write new file, append old text file, rename file 
#######################################################################
os.remove("OutputSummary.txt")
os.rename("newfile.txt","OutputSummary.txt")

print("Output summary data updated\n")

########################################################################
# Create training and testing data
#
########################################################################

X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'], random_state = 0)

########################################################################
# Create the model and test accuracy of the model
########################################################################
knn = KNeighborsClassifier(n_neighbors = 1)
knn.fit(X_train, y_train)


########################################################################
# Outputs summary to a single text file for Project requirements
########################################################################
with open("OutputSummary.txt",'a') as f:
    f.write("\n\n########################################################################\n")
    f.write("# Output training data size\n")
    f.write("########################################################################\n")
    f.write(str(X_train.shape))
    f.write("\n\n########################################################################\n")
    f.write("# Output test data size\n")
    f.write("########################################################################\n")
    f.write(str(X_test.shape))
    f.write("\n\n########################################################################\n")
    f.write("# Output knn score\n")
    f.write("########################################################################\n")
    f.write(str(knn.score(X_test, y_test)))

########################################################################
# Test the model with dimensions to get output of iris species
# 6.9, 2.9, 4, 1.5
########################################################################
X_new = np.array([[6.9, 2.9, 4, 1.5]])


prediction = knn.predict(X_new)
print("Output species\n")
print(iris['target_names'][prediction])