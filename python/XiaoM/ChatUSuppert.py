# -*- coding: utf-8 -*-
###引用库###
import jieba
import time
import re
import sys
import datetime
import ChatUTuLingAI as cai
import random
import ChatUFUN as cf
from aip import AipSpeech
import os


# 功能性处理
def FunTF(_Cfile, _Ffile, _inputs):
    Cut_in_LI = jieba.lcut(_inputs, cut_all=False)
    flag = 0  # 对匹配正确率进行计算
    Ftrue_rate = 0.33  # 正确率(>=返回)
    while True:
        F1_Ins = _Ffile.readline().rstrip()
        F2_Ins = _Ffile.readline().rstrip()
        if F1_Ins == '#END#':
            break
        if F2_Ins == '#END#':
            break
        F_list = jieba.lcut_for_search(F1_Ins)
        if len(F_list) >= len(Cut_in_LI):
            for i in F_list:
                for j in Cut_in_LI:
                    if i == j:
                        flag += 1
        elif len(Cut_in_LI) > len(F_list):
            for i in Cut_in_LI:
                for j in F_list:
                    if i == j:
                        flag += 1
        # return_true_rate=flag/len(Cut_in_LI)
        return_true_rate1 = flag / len(Cut_in_LI)
        return_true_rate2 = flag / len(F_list)
        if len(F_list) >= len(Cut_in_LI):
            return_true_11 = return_true_rate2
        elif len(Cut_in_LI) > len(F_list):
            return_true_11 = return_true_rate1
        if return_true_11 >= Ftrue_rate:  # 成功匹配正确率
            if F2_Ins == '_time':
                if cf.Fun_time():
                    return True
            if F2_Ins == '_ip':
                if cf.Fun_ip():
                    return True
            if F2_Ins == '_ipaddr':
                if cf.Fun_ipaddr():
                    return True
            if F2_Ins == '_weather':
                if cf.Fun_Weather():
                    return True
            if F2_Ins == '_kuaidi':
                if cf.Fun_kuaidi():
                    return True
            if F2_Ins == '_zidian':
                if cf.Fun_ZD():
                    return True
            flag = 0
        else:
            flag = 0


# 输入输出处理
def ChatTF(_Cfile, _Ffile, _inputs, _Return_li):
    Chat_bool, T_re_chat = Xiaomai(_Cfile, _Ffile, _inputs, _Return_li)
    output = ''
    if Chat_bool:
        output = T_re_chat
        print(T_re_chat)
        # print(_Return_li)
    else:
        TuLing_Chat = cai.Use_Tl_xiaomai(T_re_chat, _inputs, open(r'txt\\language.txt', 'a+', encoding='UTF-8'),
                                         open(r'txt\\language.txt', 'r', encoding='UTF-8'), _Return_li)
        print(TuLing_Chat)
        output = TuLing_Chat
    # print(output)
    # Speak(output)


def Speak(output):
    """ 你的 APPID AK SK """
    APP_ID = '14237339'
    API_KEY = 'PUmLG4e2WAWn6DOrScxwnnpc'
    SECRET_KEY = 'aORMRa60PpdEcv6qXAXA4YMmK0G8XFuX'

    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    result = client.synthesis(output, 'zh', 1, {
        'spd': '4',
        'pit': '5',
        'vol': '7',
        'per': '4'

    })

    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    # if not isinstance(result, dict):
    #     with open('auido.mp3', 'wb') as f:
    #         f.write(result)
    #
    # os.system('auido.mp3')
    # pygame.mixer.init()
    # track = pygame.mixer.music.load('auido.mp3')
    # pygame.mixer.music.play()
    # time.sleep(10)
    # pygame.mixer.music.stop()


# 小麦
def Xiaomai(_Cfile, _Ffile, _inputs, _Return_li):
    while True:
        C1_Ins = _Cfile.readline().rstrip()  # 读取第一行
        C2_Ins = _Cfile.readline().rstrip()  # 读取第二行
        # 语料库结束检测,并返回True,和语句
        if C1_Ins == '':
            if len(_Return_li) != 0:
                T_re_chat = random.choice(_Return_li)
                # print(T_re_chat)
                return True, T_re_chat
            else:
                return False, ''
            break
        if C2_Ins == '':
            if len(_Return_li) != 0:
                T_re_chat = random.choice(_Return_li)
                # print(T_re_chat)
                return True, T_re_chat
            else:
                return False, ''
            break
        # ----------------------------#
        Chat_boOL = Chat_inputs(_inputs, C1_Ins)
        if Chat_boOL:
            Chat_A = A_Chat(C2_Ins, _inputs, _Return_li)


# 输入处理
def Chat_inputs(_Cinput, _C):
    flag = 0
    Ctrue_rate = 0.80  # 对话---正确率(>=返回)
    Cinput_list = jieba.lcut(_Cinput, cut_all=False)  # 切片
    C_list = jieba.lcut(_C, cut_all=False)  # 切片
    if len(C_list) >= len(Cinput_list):  # 语料长,进行匹配
        for i in C_list:
            for j in Cinput_list:
                if i == j:
                    flag += 1
    elif len(Cinput_list) > len(C_list):  # 输入长,进行匹配
        for i in Cinput_list:
            for j in C_list:
                if i == j:
                    flag += 1
    return_true_rate1 = flag / len(Cinput_list)  # 输入长的正确匹配返回值
    if len(C_list) != 0:
        return_true_rate2 = flag / len(C_list)  # 语料长的正确匹配返回值
    if len(C_list) >= len(Cinput_list):
        return_true_T = return_true_rate2
    elif len(Cinput_list) > len(C_list):
        return_true_T = return_true_rate1
    if return_true_T >= Ctrue_rate:
        flag = 0
        return True
    else:
        flag = 0
        return False


# 输出处理
def A_Chat(_A_Chat, _INPUT, _Return_li):
    _Return_li.append(_A_Chat)
    if len(_Return_li):
        return _Return_li
    else:
        return False


def FL_H(_Cfile, _Ffile, _inputs, _Return_li):
    if FunTF(_Cfile, _Ffile, _inputs):
        pass
    else:
        ChatTF(_Cfile, _Ffile, _inputs, _Return_li)
