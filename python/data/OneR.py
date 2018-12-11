#-*- coding: utf-8 -*-
from sklearn.datasets import load_iris
import numpy as np
dataset=load_iris()
X = dataset.data
y = dataset.target
attribute_means = X.mean(axis=0)
print(attribute_means)
X_d = np.array(X >= attribute_means, dtype='int')