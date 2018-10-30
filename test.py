# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

#初始化
_j=[]
_next=[]
#
str=input('输入字符串:')
for i in range(len(str)):
    _j.append(i+1)

for i in range(len(str)):
    flag=i+1
    if flag==1:
        _next.append(0)
    elif flag==2:
        _next.append(1)
    else:
        for n in range(flag-2,0,-1):
            flag2=n
            # print(flag2)
            print(str[0:flag2])
            print(str[i-flag2:i])
    print('---')


print(_j)
print(str)
print(_next)