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


