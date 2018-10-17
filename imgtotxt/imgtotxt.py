# -*- coding: utf-8 -*-

from aip import AipOcr
from aip import AipNlp
import jieba
import calendar

#API
APP_ID = '14407442'
API_KEY = 'VQTrvnsND3KH3GFpG5HXkmG8'
SECRET_KEY = 'ziT27q1IgKQbFeAqNK2BBFPCyqaVwEiq'
client1 = AipNlp(APP_ID, API_KEY, SECRET_KEY)#文字时间匹配
client2 = AipOcr(APP_ID, API_KEY, SECRET_KEY)#图片文字识别


def Words_Result(_img):
    # 定义常量
    _Words_List = []  # 未处理的文字列表
    _Words_str = ''  # 字符串文字
    _Cutl_Worlds = []  # 裁剪后文字列表
    _Words_And_Probability = {}  # 文字和正确匹配率
    _Min_Words = 0.8
    # 初始化文字识别分类器
    # 图片处理

    # 参数传入
    _options = {
        'detect_direction': 'true',
        'language_type': 'CHN_ENG',
        'probability': 'true'
    }
    _result=client2.webImage(open(_img, 'rb').read(), _options)
    # _result = aipOcr.webImage(open(_filePath, 'rb').read(), _options)
    _Words_Result_li = _result['words_result']

    for _li in _Words_Result_li:
        _Words_List.append(_li['words'])
        _Words_And_Probability[_li['words']] = [_li['probability']['min']]

    for _dic in _Words_And_Probability:
        if _Words_And_Probability[_dic][0] < _Min_Words:
            # return False
            pass
    _Words_str = ''.join(_Words_List)
    _Cutl_Worlds = jieba._lcut_all(_Words_str)
    return _Words_str, _Cutl_Worlds


def Find_Time(_Words_str,_Cutl_Words=[]):
    # 定义常量
    _Every_Words = ''
    _Time_Words_L=[]
    _Time_Dict={
        'time':['时间','日期'],
        'Week_zhou':['周一','周二','周三','周四','周五','周六','周日',],
        'Week_xingqi':['星期一','星期二','星期三','星期四','星期五','星期六','星期日','星期天'],
        'week_libai':['礼拜一','礼拜二','礼拜三','礼拜四','礼拜五','礼拜六','礼拜天''礼拜日'],
        'time_sun':['早晨','早上','上午','中午','下午','晚上','午夜']
    }
    #

    lexer=client1.lexer(_Words_Str)
    for i in lexer['items']:
        if i['ne']=='TIME':
            _Time_Words_L.append(i['item'])
        if i['pos']=='t':
            _Time_Words_L.append(i['item'])
    if _Time_Words_L!=[]:
        #print(_Time_Words_L)
        return _Time_Words_L
    # for _Every_Words in _Cutl_Words:
    #     if _Every_Words!='':
    #         print(_Every_Words)

def Find_Calender(_Time_List):
    _Time_Calender=calendar.month(2018,2)
    print(_Time_Calender)




if __name__ == '__main__':
    _Words_Str, _Cutl_Words = Words_Result('4.png')
    _Time_Words_L=Find_Time(_Words_Str,_Cutl_Words)
    Find_Calender(_Time_Words_L)
