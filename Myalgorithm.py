# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------#
#KMP算法#
#传参:字符串,字符串
#返回:正确匹配次数
def KMP_next(_str):
    # 初始化
    _j = []
    _next = []
    flag3 = 0
    #
    str = _str
    str_l = []
    for i in range(len(str)):
        _j.append(i + 1)
    for i in range(len(str)):
        flag = i + 1
        if flag == 1:
            _next.append(0)
        elif flag == 2:
            _next.append(1)
        else:
            for n in range(flag - 2, 0, -1):
                flag2 = n
                if str[0:flag2] == str[i - flag2:i]:
                    flag3 += 1
                    _next.append(flag2 + 1)
                    # print(flag2+1)
                    break
            if flag3 == 0:
                _next.append(1)
            flag3 = 0
    for i in str:
        str_l.append(i)
    return _j, str_l, _next
def KMP(_strF, _strS):
    # 初始化
    strF = ''
    strS = ''
    strF_l = []
    jmp = 0
    TS = 0
    same = 0
    same_str = ''
    #
    if len(_strF) > len(_strS):
        strF = _strF
        strS = _strS
    else:
        strF = _strS
        strS = _strF
    _j, strS_l, _next = KMP_next(strS)
    for i in strF:
        strF_l.append(i)
    if len(strS) == 1:
        for i in strF:
            for n in strS:
                if i == n:
                    same += 1
                    same_str = i
                else:
                    pass
    else:
        for i in range(len(strF_l)):
            strF1 = strF[i]
            if jmp == 0:
                strS1 = strS[0 + TS]
                if strF1 == strS1:
                    TS += 1
                    same_str = same_str + strF1
                else:
                    jmp = _next[TS]
                    TS = 0
                    same_str = ''
            else:
                jmp -= 1
            if TS == len(strS):
                print(same_str)
                same += 1
                same_str = ''
                TS = 0

    print(same)
    return same
#-------------------------------------------------------------------------#
