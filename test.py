# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re

def T_array(_i,_T_l):


def test():
    print('输入字符串')
    _T = input()
    _T_l = []
    _j = []
    _next = []
    for i in range(len(_T)):
        _j.append(i + 1)
    for i in _T:
        _T_l.append(i)
    _dic={}
    for i in _j:
        _dic[i]=_T_l[i-1]
    for i in _j:
        if i == 1:
            _next.append(1)
        elif i == 2:
            _next.append(2)
        else:
            T_array(i,_T_l)

    print(_j)
    print(_T_l)
    print(_dic)
    print(_next)


test()
