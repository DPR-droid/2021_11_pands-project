########################################################################
# GMIT project for Programming and Scripting Module
# pands-project
# analyse.py
# Author David
########################################################################

########################################################################
# Program updated 19/04/2021
# Import module, import iris.data and print data with headers
########################################################################

########################################################################
### import pandas module
########################################################################
import pandas as pd

########################################################################
### Read data file
### First line is not a header
### Add headers
########################################################################
dataset = pd.read_csv("iris.data",header=None, names=["sepal.length","sepal.width","petal.length","petal.width","species"])

########################################################################
# Get the means of the observable means for two species
########################################################################

# Group by Species
gk = dataset.groupby('species')

print("Table II observable means for two species")

print("Setosa")
# Display the means of the Iris-setosa
print(gk.get_group('Iris-setosa').mean())

print("versicolor")
# Display the means of the Iris-versicolor
print(gk.get_group('Iris-versicolor').mean())
