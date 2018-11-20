# -*- coding: utf-8 -*-

import importlib
from numpy import *
import operator
import kNN

importlib.reload(kNN)
group,labels=kNN.createDataSet()
print(kNN.classify0([0,0],group,labels,3))