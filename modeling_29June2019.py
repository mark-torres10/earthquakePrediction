#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 18:56:17 2019

@author: mark
"""
"""
GOAL: Predict earthquake intensity for DrivenData competition

Approaches I'll use: 

1. catboost algorithm
2. neural network

I will: 

1. Import data
2. Fit model
3. Create predictions

"""

# import dependencies
import catboost
import numpy as np
import pandas as pd

#  1. Import data

# train data
trainData_total = pd.read_csv("train_values.csv")
y = pd.read_csv("train_labels.csv")
cat_features = [8, 9, 10, 11, 12, 13, 14, 26]

# test data
testData = pd.read_csv("test_values.csv")


#  2. Fit catboost classifier

from catboost import CatBoostClassifier, Pool
 
#  3. create training data
train_data = Pool(data = trainData_total, 
                 label = y, 
                 cat_features = cat_features)

#  4. create classifier
mod_catboost = CatBoostClassifier(iterations = 100, loss_function = "MultiClass")

#  5. fit to training data
mod_catboost.fit(train_data)

#  6. fit to test data
preds = mod_catboost.predict(testData)





