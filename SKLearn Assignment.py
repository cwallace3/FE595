import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import statsmodels.api as sm

import seaborn as sns
sns.set_style("whitegrid")
sns.set_context("poster")

from sklearn.datasets import load_boston
boston=load_boston()

# Return the size of the dataset
#print(boston.data.shape)
# (506, 13) 506 rows of data with 13 columns

# Names of the columns
#print(boston.feature_names)

# Data Set Characteristics
#print(boston.DESCR)

bos=pd.DataFrame(boston.data)
print(bos.head())

bos.columns=boston.feature_names
print(bos.head())

# To include PRICE in data frame
print(boston.target.shape)

bos['PRICE']=boston.target
print(bos.head())

# Split train-test dataset

X=bos.drop('PRICE', axis=1)
Y=bos['PRICE']

correlation_matrix=bos.corr().round(2)
# annot = True to print the values inside the square
sns.heatmap(data=correlation_matrix, annot=True, annot_kws={"size":12})


# The greatest effect on the price of a house in Boston

# Based on the correlation matrix, the infuence with the greatest effect on
# price of a house in Boston is LSTAT (% lower status of the population) with
# a value of -0.74.

# The least effect on the price of a house in Boston

# The infuence with the greatest effect on price of a house in Boston is
# DIS (weighted distances to five Boston employment centres) with a value of
# 0.25*

# * Note that CHAS (Charles River dummy variable) has a lower overall value of 
# 0.18 but it is a binary variable for "1 if tract bounds river; 0 otherwise"