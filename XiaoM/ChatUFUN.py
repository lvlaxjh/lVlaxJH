# -*- coding: utf-8 -*-import requests
import json
import jieba
import time
import re
import sys
import datetime
import socket
import urllib.request
import subprocess
import json
import urllib
import pinyin
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def Fun_time():
    print('现在时间是:' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    return True

def Fun_ip():
    # 查看当前主机名
    print('主机名称为 : ' + socket.gethostname())
    # 根据主机名称获取当前IP
    print('主机的IP为: ' + socket.gethostbyname(socket.gethostname()))
    addrs = socket.getaddrinfo(socket.gethostname(),None)

    my_ip = urllib.request.urlopen('http://pv.sohu.com/cityjson?ie=utf-8')
    ip_str = str(my_ip.read(), encoding = "utf8")
    print('公网ip为:',ip_str[ip_str.find('cip') + 7 : ip_str.find('cid') - 4])
    return True

def Fun_ipaddr():
    my_ip = urllib.request.urlopen('http://pv.sohu.com/cityjson?ie=utf-8')
    ip_str = str(my_ip.read(), encoding = "utf8")

    #print('所在城市:'+ip_str[ip_str.find('cname')+9 : -3])
    url = 'http://restapi.amap.com/v3/ip?key=40e32e3577313106aa03f5baa947a23e&ip=' + ip_str[ip_str.find('cip') + 7 : ip_str.find('cid') - 4]
    openurl = urllib.request.urlopen(url)
    addr_str = str(openurl.read(),encoding = "utf8")
    if addr_str[addr_str.find('status') + 9:addr_str.find('info') - 3] == '0':
        print('小麦没有找到你的城市')
    if addr_str[addr_str.find('status') + 9:addr_str.find('info') - 3] == '1':
        print('所在省份:',addr_str[addr_str.find('province') + 11:addr_str.find('city') - 3])
        print('所在城市:',addr_str[addr_str.find('city') + 7:addr_str.find('adcode') - 3])
        print('城市经纬度:',addr_str[addr_str.find('rectangle') + 12:-2])

    return True

def Fun_Weather():
    my_ip = urllib.request.urlopen('http://pv.sohu.com/cityjson?ie=utf-8')
    ip_str = str(my_ip.read(), encoding = "utf8")
    #print('所在城市:'+ip_str[ip_str.find('cname')+9 : -3])
    url = 'http://restapi.amap.com/v3/ip?key=40e32e3577313106aa03f5baa947a23e&ip=' + ip_str[ip_str.find('cip') + 7 : ip_str.find('cid') - 4]
    openurl = urllib.request.urlopen(url)
    addr_str = str(openurl.read(),encoding = "utf8")
    city = '(.*)' + addr_str[addr_str.find('city') + 7:addr_str.find('adcode') - 4] + '(.*?) .*'
    print(addr_str[addr_str.find('city') + 7:addr_str.find('adcode') - 4])
    with open(r'txt\\qixiang.txt','r',encoding='UTF-8') as file_obj:
        for f_line in file_obj:
            filestr = f_line.rstrip()
            if re.search(city,filestr,re.M | re.S | re.X):
                num_city = re.search(city,filestr,re.M | re.S | re.X).group()
                url = 'http://www.weather.com.cn/weather/' + num_city[:9] + '.shtml'
                resp = urlopen(url)
                soup = BeautifulSoup(resp,'html.parser')
                tagToday = soup.find('p',class_="tem")  #第一个包含class="tem"的p标签即为存放今天天气数据的标签
                try:
                    temperatureHigh = tagToday.span.string  #有时候这个最高温度是不显示的，此时利用第二天的最高温度代替。
                except AttributeError as e:
                    temperatureHigh = tagToday.find_next('p',class_="tem").span.string  #获取第二天的最高温度代替
                temperatureLow = tagToday.i.string  #获取最低温度
                weather = soup.find('p',class_="wea").string #获取天气

                print('最低温度:' + temperatureLow)
                print('最高温度:' + temperatureHigh)
                print('天气:' + weather)
            #else:
                #print('主人还是自己抬头看看天气吧,小麦没有发现主人这里的天气.')
                #break
    return True

def Fun_kuaidi():
    kuaidi_str = input('输入您的快递公司~')
    kd_list = ['申通快递','EMS邮政快递','顺丰速运','圆通快递','中通快递','韵达快递','天天快递','汇通快递','全峰快递','德邦物流','宅急送']
    kd_dict = {1:'shentong',2:'ems',3:'shunfeng',4:'yuantong',5:'zhongtong',6:'yunda',7:'tiantian',8:'huitong',9:'quanfeng',10:'debang',11:'zhaijisong'}
    num = 1
    for kdl in kd_list:
        SeaKd = re.search(kuaidi_str,kdl,re.M | re.S | re.X | re.I)
        if SeaKd != None:
            print(kdl)
            postid = input("请输入你的快递号~")
            type = kd_dict[num]

            url = 'http://www.kuaidi100.com/query?type=%s&postid=%s' % (type, postid)
            print(url)
            rs = requests.get(url)
            #将拿回的json字符串转换为python中的字典
            kd_info = json.loads(rs.text)
            #取出服务器返回的message消息，判断是否正常
            msg = kd_info['message']
            if msg == 'ok':
                print('您的快递%s信息如下：' % postid)
            # 取出快递物流信息列表
                data = kd_info['data']
                for msg in data:
                    time = msg['time']
                    context = msg['context']
                    print('时间：%s %s' % (time,context))
                else:
                    if msg == '参数错误':
                        print('您输入的快递单号有误，请检查后重新输入！')
                    else:
                        print(msg)
            break
        else:
            #print("小麦没有找到这家快递公司呀Q.Q")
            pass
        num+=1
    return True

def Fun_ZD():
    ZD_f = open(r'txt\zidian.txt','r',encoding='UTF-8')
    sea = input("你想查什么说吧~")
    while True:
            S1_Ins = ZD_f.readline().rstrip()
            S2_Ins = ZD_f.readline().rstrip()
            if S1_Ins == '#END#':
                break
            if S2_Ins == '#END#':
                break
            if sea == S1_Ins:
                print(S2_Ins)
            #else:
            #    print("小麦好像没有找到这个...")
            #    break
    return True