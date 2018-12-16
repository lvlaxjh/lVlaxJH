#-*- coding: utf-8 -*-
# from sklearn.datasets import load_iris
# import numpy as np
# dataset=load_iris()
# X = dataset.data
# y = dataset.target
# attribute_means = X.mean(axis=0)
# print(attribute_means)
# X_d = np.array(X >= attribute_means, dtype='int')
from collections import  defaultdict
from operator import  itemgetter

def train_feature_value(X,y_true,fearture_index,value):
    class_counts=defaultdict(int)
    for sample,y in zip (X,y_true):
        print(sample)
        print(y)
        if sample[fearture_index]==value:
            class_counts[y]+=1

