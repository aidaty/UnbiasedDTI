# -*- coding: utf-8 -*-
"""Preprocessing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1znN3yv9KSyRXOwMU7uoAXysnR1Z7zsRn
"""

import pickle
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.utils import resample

path= ''  # corresponding path
df=pd.read_pickle(path)

sum(df['Label'])  # number of positive samples in the dataset

###################################
# Converting dataset to X,Y format
y = df.Label
X = df.drop('Label', axis=1)

###################################
# Splitting dataset to train set (85 %)and keeping the remain 

X_train, X_remain, y_train, y_remain = train_test_split(X, y, test_size=0.15, random_state=27)
train_set = pd.concat([X_train, y_train], axis=1)
remain_set = pd.concat([X_remain, y_remain], axis=1)
train_set.to_pickle(path)
remain_set.to_pickle(path)


###################################
# Splitting remaining data to validation and test set (2.5 % validation)

y = remain_set.Label
X = remain_set.drop('Label', axis=1)
X_test, X_val, y_test, y_val = train_test_split(X, y, test_size=0.025, random_state=27)
test_set = pd.concat([X_test, y_test], axis=1)
val_set = pd.concat([X_val, y_val], axis=1)
test_set2.to_pickle(path)
val_set.to_pickle(path)

sum(train_set['Label']) # number of positive samples in the training set


###################################
# Undersampling on Negative Dataset

N = train_set[train_set.Label==0]
P = train_set[train_set.Label==1]

N_downsampled = resample(N,
                                replace = False, # sample without replacement
                                n_samples = len(P), 
                                random_state = 27) # to reproduce the samples

# combine minority and downsampled majority
downsampled = pd.concat([N_downsampled, P])

sum(downsampled['Label'])
downsampled = downsampled.sample(frac = 1)
downsampled.to_pickle(path)