# Programming and Scripting project 2021

## Introduction
The repository is created to show my research of the well-known Fisher’s Iris data set and to write the documentation for my python code to investigate.  The first objective is to create a README file that contains a summary of the dataset and investigation. 

1. Fisher’s Iris data set background
2. Use python to demonstrate its functionality
3. Investigate the Iris fisher database using python with observations
4. Test machine learning on the data set.
5. Finalise the python program for the project.
6. Conclusion

## The Fisher’s Iris data set background
### Ronald Fisher

![Ronald Fisher]( https://github.com/DPR-droid/pands-project/blob/main/README%20image%20files/Ronald%20Fisher.JPG) 

Sir Ronald Aylmer Fisher, by name R.A. Fisher, (born February 17, 1890, London, England—died July 29, 1962, Adelaide, Australia), British statistician and geneticist who pioneered the application of statistical procedures to the design of scientific experiments. [1]

### The data set
Dr E. Anderson measured the two species Iris setosa and iris versicolor growing in the same colony with the third sample Iris virginica, which differs from the two other samples in not being taken from the same natural colony [2]. The dataset fifty samples of each of the three Iris’s, with four measurements dimensions in each of the three different Iris’s
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
Python is a 4th generation language, also known as a very high-level languages.  Python's large standard library commonly cited as one of its greatest strengths provides tools suited to many tasks.

After downloading the iris data set and using just one module and two lines of code the data can be imported, read, and produce a summary of the data. 

    import pandas as pd
    data = pd.read_csv("iris.data",header=None, names=["sepal.length","sepal.width","petal.length","petal.width","variety"])
    print(data)

![Why Python 01]( https://github.com/DPR-droid/pands-project/blob/main/README%20image%20files/Why%20Python%2001.PNG)

In Table II Iris data set table excerpts by simply using the groupby function, it can be replicated the means of the setosa and versicolor irises

    gk = dataset.groupby('species')
    print(gk.get_group('Iris-setosa').mean())
    print(gk.get_group('Iris-versicolor').mean())

![ Why Python 02]( https://github.com/DPR-droid/pands-project/blob/main/README%20image%20files/Why%20Python%2002.PNG)



## An overview investigation

I wanted to do a descriptive analysis of the entire dataset and by species. The output would provide detail of the count (number of observations), mean, standard deviation of the values, minimum, 25%/50%/75% Percentiles and maximum values. This is also a simple check to verify the dataset I was working with had 150 observation with 50 observations per species.

Definition of taxonomy is the scientific study of naming, defining (circumscribing) and classifying groups of biological organisms based on shared characteristics. [3] In Python, we are going on a journey by analysing the dataset, if we can classify the groups of irises shared characteristics (sepal and petal, lengths and width) in the three different species. This project will first start using histograms, scatterplots, boxplots (and other methods if discovered during further research) to help identify these differences. This method is called Univariate analysis is the simplest form of analysing data. “Uni” means “one”, so in other words, your data has only one variable. It doesn't deal with causes or relationships (unlike regression) and its major purpose is to describe; It takes data, summarizes that data and finds patterns in the data [4]. 

### Histograms
A histogram is a plot that lets you discover, and show, the underlying frequency distribution (shape) of a set of continuous data [5]

#### Observations
The iris setosa has a noticeable difference from the other species in the petal length and width

### Boxplot
The boxplot is a type of chart often used in explanatory data analysis. Box plots visually show the distribution of numerical data and skewness through displaying the data quartiles (or percentiles) and averages.[6]

#### Observations
The iris setosa again shows a noticeable difference from the other species in the petal length and width. The iris virginica has a couple of outliers on the sepal length and width.

### Pairwise plots/scatterplot matrix
Scatter plots are used to observe relationships between variables[10]. A four by four matrix with histograms on the diagonal and scatter plots for a combination of each of the variables. 

#### Observations
The iris setosa again shows a noticeable difference from the other species in the petal length and width. The last two rows of the petal width and length show groupings with only a slight cross over in the iris virginica and Iris virginica.

### Violin 
Other researchers have shown to use a violin plot this method is test how easily it is implemented in python. A violin plot is a method of plotting numeric data. While a box plot only shows summary statistics such as mean/median and interquartile ranges, the violin plot shows the full distribution of the data. [7]

#### Observations
This seems to be a mix between histograms and boxplots, again repeating the iris setosa the petal length and width distinct difference. The iris virginica has a couple of outliers on the sepal length and width.


## Machine Learning
This again is another reason why python is suggested as a tool for data analysis. While I am only starting on my learning curve with GMIT, I can already see the benefits of using python. The module installed scikit-learn comes with a few small standard datasets that do not require downloading any file from some external website [8] and includes the Fisher iris database. Install the module using
    
    pip install -U scikit-learn

### Supervised machine learning
The method chosen for Machine Learning is called the k-nearest neighbours (KNN) algorithm. A supervised machine learning algorithm (as opposed to an unsupervised machine learning algorithm) relies on labelled input data to learn a function that produces an appropriate output when given new unlabelled data. [9]

The dataset was split into training and test data, the model was created and gave a test accuracy of 0.9736842105263158. Adding random dimensions into a NumPy array with values between the min and max of petal/sepal length and width 

    np.array([[6.9, 2.9, 4, 1.5]])

The model predicted the species of iris as: 
    
    ['versicolor']

## Python Program
The python program completes the following tasks

1. Imports modules (pandas, os, matplotlib, seaborn, sklearn, NumPy)
2. Checks if the user has the iris.data file. Informs user if present or not
3. Reads the data file and adds headers
4. Outputs data to CSV file and informs the user when completed
5. Sets the dataset for each species of iris
6. Outputs data to a single text file and informs the user when completed
7. Saves histograms, boxplot, violin and Pairwise plots/scatterplot matrix as pngs and informs the user when completed
8. Test if the user has the sklearn module installed and ends the program if not
9. Creates the data frame
10. Original text is re-written with output from the sklearn module
11. Creates the training data and tests the accuracy of the model
12. Appends summary text file and informs the user when completed
13. Allows the user to input data and test the model
14. The predicted iris species is displayed to the user
15. Program closes.

![MLTesting](https://github.com/DPR-droid/pands-project/blob/main/README%20image%20files/MLTesting.PNG)

## Conclusion
There are many outcomes from this project: 
1. The analysis of the Fisher Iris dataset would confirm the iris setosa can be distinguished using the petal length and width with minor overlap on the iris virginica and versicolor.
2. Univariate analysis (histograms, boxplots, scatterplots) when investigating to distinguishes visual patterns within the data
3. The project was a learning exercise to develop my programming skills.
4. Demonstration of Python as a tool for Data Analysis and Machine Learning. 

## Acknowledgement
Lecturer Andrew Beatty Programming and Scripting GMIT

Family and friends for their support

## References/Citations

[1] https://www.britannica.com/biography/Ronald-Aylmer-Fisher

[2] https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1469-1809.1936.tb02137.x

[3] https://en.wikipedia.org/wiki/Taxonomy_(biology)

[4] https://www.statisticshowto.com/univariate/

[5] https://statistics.laerd.com/statistical-guides/understanding-histograms.php

[6] https://www.simplypsychology.org/boxplots.html

[7] https://en.wikipedia.org/wiki/Violin_plot

[8] https://scikit-learn.org/stable/datasets/toy_dataset.html

[9] https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761

[10] https://chartio.com/learn/charts/what-is-a-scatter-plot/


## Tools / Resources used

http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data

https://stackoverflow.com/questions/14494747/how-to-add-images-to-readme-md-on-github

https://stackoverflow.com/questions/34091877/how-to-add-header-row-to-a-pandas-dataframe

https://numpy.org/

https://www.geeksforgeeks.org/python-pandas-dataframe-groupby/

https://stackoverflow.com/questions/15777951/how-to-suppress-pandas-future-warning

https://blog.usejournal.com/exploratory-data-analysis-72d596620e31

https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d

https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166

https://seaborn.pydata.org/tutorial/axis_grids.html

https://scikit-learn.org/stable/tutorial/basic/tutorial.html

https://scikit-learn.org/stable/install.html

https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris

https://translate.google.com/translate?sl=auto&tl=en&u=https://paulovasconcellos.com.br/como-criar-seu-primeiro-aplicativo-de-machine-learning-7b6af291ba11

https://www.kaggle.com/marcelotournier/iris-dataset-machine-learning-exercise

https://matplotlib.org/3.1.1/gallery/ticks_and_spines/ticklabels_rotation.html

https://stackoverflow.com/questions/1051254/check-if-python-package-is-installed

https://www.w3schools.com/python/python_file_remove.asp

https://stackoverflow.com/questions/5914627/prepend-line-to-beginning-of-a-file

https://stackoverflow.com/questions/48230230/typeerror-mismatch-between-array-dtype-object-and-format-specifier-18e/48231106

https://www.askpython.com/python/array/print-an-array-in-python

### Images
 
https://en.wikipedia.org/wiki/Ronald_Fisher

https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1469-1809.1936.tb02137.x
    
https://www.kaggle.com/vinayshaw/iris-species-100-accuracy-using-naive-bayes




