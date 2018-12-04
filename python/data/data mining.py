#-*- coding: utf-8 -*-
import xlrd
import re


file_excel='data.xlsx'#文件
data =xlrd.open_workbook(file_excel)
# print(data.sheet_names())
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
# print(nrows)
colval = 13
all=[]
for i in range(0, nrows):
    bol=False
    temp = table.col_values(colval)[i]
    if temp=='':
        all.append('no')
    else:
        all.append(temp)


# print(all)
alld=len(all)
one=0
for i in all:
    if i!='no':
        for n in all:
            if n != 'no':
                if i==n:
                    one+=1
        print((one/alld))
        one=0
    else:
        print(0)

