
import pandas as pd

# Read data from archive.ics.uci.edu
data = pd.read_csv("iris.data",header=None)

# Print data
print(data)