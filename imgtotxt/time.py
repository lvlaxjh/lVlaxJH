# -*- coding: utf-8 -*-

from aip import AipOcr
from aip import AipNlp
import jieba
import calendar
import time

# API
APP_ID = '14407442'
API_KEY = 'VQTrvnsND3KH3GFpG5HXkmG8'
SECRET_KEY = 'ziT27q1IgKQbFeAqNK2BBFPCyqaVwEiq'
client1 = AipNlp(APP_ID, API_KEY, SECRET_KEY)  # 文字时间匹配
client2 = AipOcr(APP_ID, API_KEY, SECRET_KEY)  # 图片文字识别


# 图片提取文字(返回:正确,字符串)
def Words_Result(_img):
    # 定义常量
    _Words_List = []  # 未处理的文字列表
    _Words_str = ''  # 字符串文字
    _Cutl_Worlds = []  # 裁剪后文字列表
    _Words_And_Probability = {}  # 文字和正确匹配率
    _Min_Words = 0.8  # 最小文字正确度
    # 参数传入
    _options = {
        'detect_direction': 'true',
        'language_type': 'CHN_ENG',
        'probability': 'true'
    }
    _result = client2.webImage(open(_img, 'rb').read(), _options)  # 提取文字
    _Words_Result_li = _result['words_result']
    for _li in _Words_Result_li:
        _Words_List.append(_li['words'])
        _Words_And_Probability[_li['words']] = [_li['probability']['min']]
    for _dic in _Words_And_Probability:
        if _Words_And_Probability[_dic][0] < _Min_Words:
            return False, ''
    _Words_str = ''.join(_Words_List)
    return True, _Words_str


# 文字时间提取
def Find_Time(_Words_str):
    # 定义常量
    _Every_Words = ''
    _Time_Words_L = []
    _Time_Dict = {
        'time': ['时间', '日期'],
        'Week_zhou': ['周一', '周二', '周三', '周四', '周五', '周六', '周日', ],
        'Week_xingqi': ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日', '星期天'],
        'week_libai': ['礼拜一', '礼拜二', '礼拜三', '礼拜四', '礼拜五', '礼拜六', '礼拜天''礼拜日'],
        'time_sun': ['早晨', '早上', '上午', '中午', '下午', '晚上', '午夜']
    }
    #

    lexer = client1.lexer(_Words_Str)
    for i in lexer['items']:
        if i['ne'] == 'TIME':
            _Time_Words_L.append(i['item'])
        if i['pos'] == 't':
            _Time_Words_L.append(i['item'])
    if _Time_Words_L != []:
        return _Time_Words_L


def Find_Calender(_Time_List):
    # 常量
    _Time_Calender = ''
    _Time_Now = ''
    _Time_Now_Dict = {
        'year': '',
        'month': '',
        'day': '',
        'time': ''
    }


    print(_Time_List)
    _Time_Now = time.strftime('%Y~%m-%d=%H:%M:%S', time.localtime(time.time()))
    _Time_Now_Dict['year'] = _Time_Now[:_Time_Now.find('~')]
    _Time_Now_Dict['month'] = _Time_Now[_Time_Now.find('~') + 1:_Time_Now.find('-')]
    _Time_Now_Dict['day'] = _Time_Now[_Time_Now.find('-') + 1:_Time_Now.find('=')]
    _Time_Now_Dict['time'] = _Time_Now[_Time_Now.find('=') + 1:]
    return int(_Time_Now_Dict['year']),int(_Time_Now_Dict['month']),int(_Time_Now_Dict['day']),_Time_Now_Dict['time']
    # _Time_Calender = calendar.month(int(_Time_Now_Dict['year']),int (_Time_Now_Dict['month']))
    # print(_Time_Calender)

if __name__ == '__main__':

    Words_TF, _Words_Str = Words_Result('1.png')
    if Words_TF:
        _Time_Words_L = Find_Time(_Words_Str)
        year,month,day,time=Find_Calender(_Time_Words_L)
        # print(year, month, day, time)

