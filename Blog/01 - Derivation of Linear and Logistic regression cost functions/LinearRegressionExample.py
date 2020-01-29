"""Example of Linear Regression.
    Just an example of linear regression application.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
y = iris.target

flowers = iris.target_names
features = iris.feature_names

sepal_length_setosa = X[:, 0][:50]
sepal_width_setosa = X[:, 1][:50]
sepal_length_versicolor = X[:, 0][50:100]
sepal_width_versicolor = X[:, 1][50:100]
sepal_length_virginica = X[:, 0][100:150]
sepal_width_virginica = X[:, 1][100:150]

petal_length_setosa = X[:, 2][:50]
petal_width_setosa = X[:, 3][:50]
petal_length_versicolor = X[:, 2][50:100]
petal_width_versicolor = X[:, 3][50:100]
petal_length_virginica = X[:, 2][100:150]
petal_width_virginica = X[:, 3][100:150]

## ================ ##
## EXPLORATORY_PART ##
## ================ ##

plt.figure(figsize=(20,14))
plt.scatter(x=sepal_length_setosa,
            y=sepal_width_setosa,
            label='Setosa',
            alpha=.75)
plt.scatter(x=sepal_length_versicolor,
            y=sepal_width_versicolor,
            label='Versicolor',
            alpha=.75)
plt.scatter(x=sepal_length_virginica,
            y=sepal_width_virginica,
            label='Virginica',
            alpha=.75)
plt.title('Iris Linear Regression (Sepal)')
plt.xlabel('Sepal length')
plt.ylabel('Sepal width')
plt.legend()
plt.savefig('visualizations/SepalScatterplot.png')
plt.show()

plt.figure(figsize=(20,14))
plt.scatter(x=petal_length_setosa,
            y=petal_width_setosa,
            label='Setosa',
            alpha=.75)
plt.scatter(x=petal_length_versicolor,
            y=petal_width_versicolor,
            label='Versicolor',
            alpha=.75)
plt.scatter(x=petal_length_virginica,
            y=petal_width_virginica,
            label='Virginica',
            alpha=.75)
plt.title('Iris Linear Regression (Petal)')
plt.xlabel('Petal length')
plt.ylabel('Petal width')
plt.legend()
plt.savefig('visualizations/PetalScatterplot.png')
plt.show()

## estaría super bien poder printar las tres rectas de regresion juntas por especie
