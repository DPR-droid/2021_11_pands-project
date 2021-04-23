# Programming and Scripting project 2021

## Introduction
The repository is created to show my research of the well-known Fisher’s Iris data set and to write the documentation for my python code to investigate.  The first objective is to create a README file which contains a summary of the dataset and investigation. 

1.	Fisher’s Iris data set background

## The Fisher’s Iris data set background
### Ronald Fisher

![Ronald Fisher]( https://github.com/DPR-droid/pands-project/blob/main/README%20image%20files/Ronald%20Fisher.JPG)

Sir Ronald Aylmer Fisher, byname R.A. Fisher, (born February 17, 1890, London, England—died July 29, 1962, Adelaide, Australia), British statistician and geneticist who pioneered the application of statistical procedures to the design of scientific experiments. [1]

### The data set
Dr E. Anderson measured the two species Iris setosa and iris versicolor growing in the same colony with the third sample Iris virginica, differs from the two other samples in not being taken from the same natural colony [2]. The dataset fifty samples of each of the three Iris’s, with four measurements dimensions in each of the three different Iris’s
1.	Sepal Length
2.	Sepal width
3.	Petal Length
4.	Petal width

 ![Illustration of measurement of sepal and petal on the three species of irises](https://github.com/DPR-droid/pands-project/blob/main/README%20image%20files/Iris%20Sepal%20and%20Petal.PNG)

The dataset was first used by Ronald Fisher in 1936 in his paper “The use of multiple measurements in taxonomic problems”. The idea proposed by Fisher is linear discriminant: “WHEN two or more populations have been measured in several characters, xl, ... , x8, special interest attaches to certain linear  functions of the measurements  by which the populations are best discriminated.” [2]  


### Iris data set table excerpts

![ Table I shows measurements of the flowers of fifty plants]( https://github.com/DPR-droid/pands-project/blob/main/README%20image%20files/Table%201.PNG)

![ The observed means and their differences are shown in Table 11. The sums of squares and products of deviations  from the specific means are shown in Table 111.]( https://github.com/DPR-droid/pands-project/blob/main/README%20image%20files/Table%202.PNG)

## Why Python for this project
Python is a 4th generation languages, also known as very high level languages.  Python's large standard library, commonly cited as one of its greatest strengths, provides tools suited to many tasks.

After downloading the iris data set and using just one module and two lines of code the data can be imported, read, and produce a summary of the data. 

    import pandas as pd
    data = pd.read_csv("iris.data",header=None, names=["sepal.length","sepal.width","petal.length","petal.width","variety"])
    print(data)

![Why Python 01]( https://github.com/DPR-droid/pands-project/blob/main/README%20image%20files/Why%20Python%2001.PNG)

On Table 11 Iris data set table excerpts by simply using the groupby function it can be replicated the means of the setosa and versicolor irises

    gk = dataset.groupby('species')
    print(gk.get_group('Iris-setosa').mean())
    print(gk.get_group('Iris-versicolor').mean())

![ Why Python 02]( https://github.com/DPR-droid/pands-project/blob/main/README%20image%20files/Why%20Python%2002.PNG)

The file was renamed to whypython.py 

## An overview investigation

I wanted to do a descriptive analysis of the entire dataset and by species. The output would provide detail of the count (number of observations), mean, standard deviation of the values, minimum, 25%/50%/75% Percentiles and maximum values. This is also a simple check to verify the dataset I was working with had 150 observation with 50 observations per species.

Definition of taxonomy is the scientific study of naming, defining (circumscribing) and classifying groups of biological organisms based on shared characteristics. In Python, we are going on a journey by analysing the dataset, if we can classify the groups of irises shared characteristics (sepal and petal, lengths and width) in the three different species. This project will first start using histograms, scatterplots, boxplots (and other methods if discovered during further research) to help identify these differences. This method is called Univariate analysis is the simplest form of analysing data. “Uni” means “one”, so in other words your data has only one variable. It doesn't deal with causes or relationships (unlike regression) and its major purpose is to describe; It takes data, summarizes that data and finds patterns in the data [4]. If times allow and we will see if we can use predictive analysis to identify the species of Iris

### Histograms
Histogram is a plot that lets you discover, and show, the underlying frequency distribution (shape) of a set of continuous data [5]

#### Observations
    The iris setosa has a noticeable difference from the other species in the petal length and width

### Boxplot
The boxplot is a type of chart often used in explanatory data analysis. Box plots visually show the distribution of numerical data and skewness through displaying the data quartiles (or percentiles) and averages.[6]

#### Observations
    The iris setosa again shows a noticeable difference from the other species in the petal length and width. The iris virginica has a couple of outliers on the sepal lenght and width.

### Pairwise plots/scatterplot matrix
With four lines of code in python gives a four by four matrix with histograms on the diagonal and scatter plots for a combination of each of the variables. 

#### Observations
    The iris setosa again shows a noticeable difference from the other species in the petal length and width. The last two rows of the petal width and lenght show groupings with only slight cross over in the iris virginica and iris virginica .

### Violin 
Other researchers have shown to use a violin plot this method is test how easily it is implimented in python. A violin plot is a method of plotting numeric data. It is similar to a box plot, with the addition of a rotated kernel density plot on each side. ... While a box plot only shows summary statistics such as mean/median and interquartile ranges, the violin plot shows the full distribution of the data.

#### Observations
    This seems to be a mix between histograms and boxplots, futher research is required to understand the output.

## Acknowledgement
Lecturer Andrew Beatty Programming and Scripting GMIT


## References/Citations

[1] https://www.britannica.com/biography/Ronald-Aylmer-Fisher

[2] https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1469-1809.1936.tb02137.x

[3] https://en.wikipedia.org/wiki/Taxonomy_(biology)

[4] https://www.statisticshowto.com/univariate/

[5] https://statistics.laerd.com/statistical-guides/understanding-histograms.php

[6] https://www.simplypsychology.org/boxplots.html

[7] https://en.wikipedia.org/wiki/Violin_plot


## Tools/ Resources

http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

https://stackoverflow.com/questions/14494747/how-to-add-images-to-readme-md-on-github

https://stackoverflow.com/questions/34091877/how-to-add-header-row-to-a-pandas-dataframe

https://numpy.org/

https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/

https://blog.usejournal.com/exploratory-data-analysis-72d596620e31

https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d

https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166

https://seaborn.pydata.org/tutorial/axis_grids.html

### Images
 
https://en.wikipedia.org/wiki/Ronald_Fisher

https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1469-1809.1936.tb02137.x
    
https://www.kaggle.com/vinayshaw/iris-species-100-accuracy-using-naive-bayes




