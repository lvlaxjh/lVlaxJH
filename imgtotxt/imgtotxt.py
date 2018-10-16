# -*- coding: utf-8 -*-

from aip import AipOcr
import jieba

def Words_Result(_filePath):
    try:
        open(_filePath, 'rb')
    except OSError as reason:
        print('Errorl1' + str(reason))
        exit(1)
    # 定义常量
    APP_ID = '14407442'
    API_KEY = 'VQTrvnsND3KH3GFpG5HXkmG8'
    SECRET_KEY = 'ziT27q1IgKQbFeAqNK2BBFPCyqaVwEiq'
    #
    _Words_List=[]#未处理的文字列表
    _Words_str=''#字符串文字
    _Cutl_Worlds=[]#裁剪后文字列表
    _Words_And_Probability={}#文字和正确匹配率
    _Min_Words=0.8
    # 初始化文字识别分类器
    aipOcr=AipOcr(APP_ID, API_KEY, SECRET_KEY)
    # 读取图片
    _options = {
        'detect_direction': 'true',
        'language_type': 'CHN_ENG',
        'probability':'true'
    }
    _result = aipOcr.webImage(open(_filePath, 'rb').read(),_options)
    _Words_Result_li=_result['words_result']

    for _li in _Words_Result_li:
        _Words_List.append(_li['words'])
        _Words_And_Probability[_li['words']]=[_li['probability']['min']]

    for _dic in _Words_And_Probability:
        if _Words_And_Probability[_dic][0]<_Min_Words:
            return False

    _Words_str=''.join(_Words_List)
    _Cutl_Worlds=jieba._lcut_all(_Words_str)
    return _Words_str,_Cutl_Worlds





if __name__=='__main__':
    Words_Result('1.png')