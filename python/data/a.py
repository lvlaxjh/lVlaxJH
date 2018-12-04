#-*- coding: utf-8 -*-
import xlrd
import re



def readExcel():
    data = xlrd.open_workbook('01.xlsx')
    table = data.sheets()[0]    # 打开第一张表
    nrows = table.nrows         # 获取表的行数
    ncols = table.ncols
    colval = 13

    for i in range(0,nrows):
        temp = table.col_values(colval)[i]
        index = 1
        result = 0
        res = 0
        #result = list(map(int, result)) #字符串转化为数字


        if temp.find('囊')!= -1:
                result = 1

        else:
                result = 0

        print(result)

if __name__ == '__main__':
    readExcel()