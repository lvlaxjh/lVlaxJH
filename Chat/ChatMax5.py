# -*- coding: utf-8 -*-
#暂不支持英文对话
###引用库###
###############
import jieba
import time
import re
import sys
import datetime
import requests
import CSuppert6
if __name__ == "__main__":
    try:
        response = requests.get('http://www.lvlaxjh.com/', timeout=5)
    except requests.exceptions.ConnectionError:
        print('ConnectionError')
        exit(1)
    except requests.exceptions.Timeout:
        print('Timeout')
        exit(1)
    try:
        l1file = open(r'txt\language.txt','r',encoding='UTF-8')
        #print('open')
    except OSError as reason:
        print('Errorl1' + str(reason))
        time.sleep(3)
        exit(1)
    l1file.close()
    try:
        f1file = open(r'txt\Function.txt','r',encoding='UTF-8')
        #print('open')

    except OSError as reason:
        print('Errorf1' + str(reason))
        time.sleep(3)
        exit(1)
    f1file.close()

    Return_list=[]

    while True:
        Chat_input = input('you speak(p)~~::')#用户输入
        print('你-----------------------------:')
        print(Chat_input)
        print('小麦---------------------------:')
        if len(Chat_input) == 0:
            print('此时无声胜有声')
        elif Chat_input != 'p':
            if re.match('(.*) 饕餮 (.*?) .*',Chat_input,re.M | re.S | re.X):
                print('进入控制台')
            else:
                CSuppert6.FL_H(open(r'txt\language.txt','r',encoding='UTF-8'), open(r"txt\Function.txt", 'r', encoding='UTF-8'), Chat_input, Return_list)
                Return_list=[]
        else:
            exit(1)