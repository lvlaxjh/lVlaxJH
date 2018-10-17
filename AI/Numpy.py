# -*- coding: utf-8 -*-
import numpy as np
# 从列表中获得迭代器
import numpy as np
list = range(5)
it = iter(list)
# 使用迭代器创建 ndarray
x = np.fromiter(it, dtype =  float)
print (x)



