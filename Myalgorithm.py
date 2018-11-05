# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# KMP algorithm
# 传参:字符串(str),字符串(str)
# 返回:正确匹配次数(int)
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


# -------------------------------------------------------------------------
# 栈#
class Stack:
    def __init__(self):
        self.__stack = []
        pass

    # 入栈
    # 传参:入栈内容(all)
    # 返回:栈(list)
    def Push(self, Content):
        self.__stack.append(Content)
        return self.__stack

    # 出栈
    # 传参:无
    # 返回:出栈内容(all)/若栈为空:返回False(bool)
    def Pop(self):
        if self.__stack == []:
            return False
        this_pop = self.pop
        return this_pop

    # 求栈长度
    # 参数:无
    # 返回:栈长度(int)
    def Size(self):
        size = len(self.__stack)
        return size

    # 清空栈
    # 传参:无
    # 返回:None
    def Delete(self):
        del self.__stack[:]
        return None

    # 完整栈
    # 传参:无
    # 返回:栈(list)
    def Show(self):
        return self.__stack


# -------------------------------------------------------------------------
# GCD algorithm
# 传参:整数(int),整数(int)
# 返回:最大公约数(int)
# 相除法
def Division_GCD(Num1, Num2):
    if Num2 > Num1:
        flag = Num1
        Num1 = Num2
        Num2 = flag
    while (True):
        Remainder = Num1 % Num2
        if Remainder == 0:
            return Num2
        else:
            Num1 = Num2
            Num2 = Remainder


# 相减法
def Subtraction_GCD(Num1, Num2):
    while (True):
        if Num2 > Num1:
            flag = Num1
            Num1 = Num2
            Num2 = flag
        Num1 = Num1 - Num2
        if Num1 == Num2:
            return Num1


# 穷举法
def Exhaustive_GCD(Num1, Num2):
    if Num2 > Num1:
        flag = Num1
        Num1 = Num2
        Num2 = flag
    flag = Num2
    while (True):
        if Num1 % flag == 0 and Num2 % flag == 0:
            return flag
        flag -= 1


# -------------------------------------------------------------------------
# LCM algorithm
# 传参:整数(int),整数(int)
# 返回:最小公倍数(int)
def LCM(Num1, Num2):
    return int((Num1 * Num2) / Division_GCD(Num1, Num2))

# -------------------------------------------------------------------------
# 24Point
