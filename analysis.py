
import pandas as pd

# Read data from archive.ics.uci.edu
data = pd.read_csv("iris.data",header=None, names=["sepal.length","sepal.width","petal.length","petal.width","variety"])

# Print data
print(data)