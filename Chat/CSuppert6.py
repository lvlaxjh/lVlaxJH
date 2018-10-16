# -*- coding: utf-8 -*-
###引用库###
import jieba
import time
import re
import sys
import datetime
import TuLingAI
import random
import FUN

#输入处理
def Chat_inputs(_Cinput,_C):
    flag = 0
    #
    Ctrue_rate = 0.75#对话---正确率(>=返回)
    #
    Cinput_list = jieba.lcut(_Cinput,cut_all=False)
    C_list = jieba.lcut(_C,cut_all=False)
    if len(C_list) >= len(Cinput_list):
        for i in C_list:
            for j in Cinput_list:
                if i == j:
                    flag+=1
    elif len(Cinput_list) > len(C_list):
        for i in Cinput_list:
            for j in C_list:
                if i == j:
                    flag+=1
    return_true_rate1 = flag / len(Cinput_list)
    if len(C_list) != 0:
        return_true_rate2 = flag / len(C_list)
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
#输出处理
def A_Chat(_A_Chat,_INPUT,_Return_li):
    Cut_in_LI = jieba.lcut(_INPUT,cut_all=False)
    Cut_C_li = jieba.lcut(_A_Chat,cut_all=False)
    _Return_li.append(_A_Chat)
    #print(_Return_li)
    #T_re_chat=random.choice(_Return_li)
    #print(T_re_chat)
    if len(_Return_li):
        return _Return_li
    else:
        return 'NONE'
    #flag = 0
    #层1
    #if len(Cut_C_li) >= len(Cut_in_LI):
    #    for i in Cut_C_li:
    #        for j in Cut_in_LI:
    #            if i == j:
    #                flag+=1
    #elif len(Cut_in_LI) > len(Cut_C_li):
    #    for i in Cut_in_LI:
    #        for j in Cut_C_li:
    #            if i == j:
    #                flag+=1
    #if flag >= 1:
    #    return _A_Chat
    #else:
    #   return 'NONE'
#功能性处理
def FunTF(_Cfile,_Ffile,_inputs):
    Cut_in_LI = jieba.lcut(_inputs,cut_all=False)
    flag = 0#对匹配正确率进行计算
    Ftrue_rate = 0.33#正确率(>=返回)
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
                        flag+=1
        elif len(Cut_in_LI) > len(F_list):
            for i in Cut_in_LI:
                for j in F_list:
                    if i == j:
                        flag+=1
        #return_true_rate=flag/len(Cut_in_LI)
        return_true_rate1 = flag / len(Cut_in_LI)
        return_true_rate2 = flag / len(F_list)
        if len(F_list) >= len(Cut_in_LI):
            return_true_11 = return_true_rate2
        elif len(Cut_in_LI) > len(F_list):
            return_true_11 = return_true_rate1
        if return_true_11 >= Ftrue_rate: #成功匹配正确率
            if F2_Ins == '_time':
                if FUN.Fun_time():
                    return True
            if F2_Ins == '_ip':
                if FUN.Fun_ip():
                    return True
            if F2_Ins == '_ipaddr':
                if FUN.Fun_ipaddr():
                    return True
            if F2_Ins == '_weather':
                if FUN.Fun_Weather():
                    return True
            if F2_Ins == '_kuaidi':
                if FUN.Fun_kuaidi():
                    return True
            if F2_Ins == '_zidian':
                if FUN.Fun_ZD():
                    return True
            flag = 0
        else:
            flag = 0
#输入输出处理
def ChatTF(_Cfile,_Ffile,_inputs,_Return_li):
    flag = 0#对匹配正确率进行计算
    Ctrue_rate = 0.80#正确率(>=返回)
    Use_C = 0#选择语言使用~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    if Use_C == 0:
            print(TuLingAI.Use_Tl_xiaomai(_inputs,open(r'txt\\language.txt','a+',encoding='UTF-8'),open(r'txt\\language.txt','r',encoding='UTF-8')))
    elif Use_C == 1:
        while True:
            C1_Ins = _Cfile.readline().rstrip()
            C2_Ins = _Cfile.readline().rstrip()
            #if C1_Ins == '#END#':
            #    break
            #if C2_Ins == '#END#':
            #    break
            if  not C1_Ins:
                if(Chat_A != 'NONE'):
                    #print(Chat_A)
                    T_re_chat=random.choice(_Return_li)
                    print(T_re_chat)
                break
            if not C2_Ins:
                if(Chat_A != 'NONE'):
                    #print(Chat_A)
                    T_re_chat=random.choice(_Return_li)
                    print(T_re_chat)
                break
            Chat_boOL = Chat_inputs(_inputs,C1_Ins)
            if Chat_boOL:
                Chat_A = A_Chat(C2_Ins,_inputs,_Return_li)
                #if(Chat_A != 'NONE'):
                #    print(Chat_A)
                    #break

def FL_H(_Cfile,_Ffile,_inputs,_Return_li):
    if FunTF(_Cfile,_Ffile,_inputs):
        pass
    else:
        ChatTF(_Cfile,_Ffile,_inputs,_Return_li)