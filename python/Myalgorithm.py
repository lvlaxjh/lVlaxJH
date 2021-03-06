# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# KMP algorithm
# 传参:字符串(str),字符串(str)
# 返回:字符串匹配位置(list)

def MY_KMP_next(_str):
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
    # return _j, str_l, _next
    return _next


def MY_KMP(_strF, _strS):
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
    _next = MY_KMP_next(strS)
    print(_next)  # //////////////////////////////////
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
                # print(same_str)
                same += 1
                same_str = ''
                TS = 0
    return same


def KMP_next(_str):
    _next = []
    j, k = 1, 0
    _next.insert(1, 0)
    while (j < len(_str)):
        if k == 0 or _str[j - 1] == _str[k - 1]:
            j += 1
            k += 1
            _next.insert(j, k)
        else:
            k = _next[k - 1]
    return _next


def KMP_Val(_str):
    _nextval = []
    j = 1
    k = 0
    _nextval.insert(0, 0)
    while (j < len(_str)):
        if k == 0 or _str[j - 1] == _str[k - 1]:
            j += 1
            k += 1
            if _str[j - 1] != _str[k - 1]:
                _nextval.insert(j - 1, k)
            else:

                if j > len(_nextval):
                    _nextval.insert(j - 1, _nextval[k - 2])
                else:
                    _nextval[j - 1] = _nextval[k - 1]
        else:
            j = _nextval[j - 1]
    return _nextval


def KMP(_strF, _strS):
    strF = ""
    strS = ""
    if len(_strF) > len(_strS):
        strF = _strF
        strS = _strS
    else:
        strF = _strS
        strS = _strF
    next = KMP_next(strS)
    Is_Find_Pos = []
    cut_len = 0
    while (True):
        i = 0
        j = 0
        if len(strF) <= len(strS):
            return Is_Find_Pos
        while (i <= len(strF) and j <= len(strS)):
            if j == 0 or strF[i - 1] == strS[j - 1]:
                i += 1
                j += 1
            else:
                j = next[j - 1]
        if j > len(strS):
            Is_Find_Pos.append(i - len(strS) + cut_len)
            strF = strF[i - len(strS) + len(strS) - 1:]
            cut_len = i - len(strS) + len(strS) - 1
        else:
            return Is_Find_Pos


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
# Permutations
# 传参:待排列列表(list)
# 返回:排列后所有(list)

def PerMain(Step, Num_List=[]):
    if len(Num_List) == Step + 1:
        print(Num_List)
        return
    else:
        for i in range(Step, len(Num_List)):
            if Is_Equal(Num_List, Step, i):
                continue
            else:
                Num_List[Step], Num_List[i] = Num_List[i], Num_List[Step]
                PerMain(Step + 1, Num_List)
                Num_List[Step], Num_List[i] = Num_List[i], Num_List[Step]


def Is_Equal(Num_List, Left, Right):
    for i in range(Left, Right):
        if Num_List[i] == Num_List[Right]:
            return True


def Permutations_T(Num_List=[]):
    Step = 0
    PerMain(Step, Num_List)


# -------------------------------------------------------------------------
# Sort
#
# Bubble Sort
def Bubble_Sort(Num_List=[]):
    for i in range(len(Num_List) - 1):
        for j in range(len(Num_List) - 1 - i):
            if Num_List[j] > Num_List[j + 1]:
                flag = Num_List[j + 1]
                Num_List[j + 1] = Num_List[j]
                Num_List[j] = flag
    return Num_List


# Selection Sort
def Selection_Sort(Num_List=[]):
    MinNum, temp = 0, 0
    for i in range(len(Num_List) - 1):
        MinNum = i
        for j in range(i + 1, len(Num_List)):
            if Num_List[j] < Num_List[MinNum]:
                MinNum = j
        temp = Num_List[i]
        Num_List[i] = Num_List[MinNum]
        Num_List[MinNum] = temp
    return Num_List


# Insertion Sort
def Insertion_Sort(Num_List=[]):
    PerIndex = 0
    Current = 0
    for i in range(1, len(Num_List)):
        PerIndex = i - 1
        Current = Num_List[i]
        while (PerIndex >= 0 and Num_List[PerIndex] > Current):
            Num_List[PerIndex + 1] = Num_List[PerIndex]
            PerIndex -= 1
        Num_List[PerIndex + 1] = Current
    return Num_List


# Shell Sort
def Shell_Sort(Num_List=[]):
    step = int(len(Num_List) / 3)
    while (step > 0):
        for i in range(step, len(Num_List)):
            while (i >= step and Num_List[i - step] > Num_List[i]):
                Num_List[i], Num_List[i - step] = Num_List[i - step], Num_List[i]
                i -= step
        step = int(step / 3)
    return Num_List


# -------------------------------------------------------------------------
# Tree
# 传参:输入(all)
# 返回:树(list)
# Binary tree---
# 创建树
def Create_Tree():
    Tree = MainN()
    return Tree


def MainN():
    Tree_List = [None, None, None]
    DataNode = input()
    if DataNode == '`':
        return None
    Tree_List[1] = DataNode
    Tree_List[0] = MainN()  # Left
    Tree_List[2] = MainN()  # Right
    return Tree_List


# 先序遍历
def Preorder_Traversal(Tree_List=[]):
    if Tree_List == None:
        return
    else:
        print(Tree_List[1])
    Preorder_Traversal(Tree_List[0])  # Left
    Preorder_Traversal(Tree_List[2])  # Right
    return Tree_List


# 中序遍历
def Inorder_Traversal(Tree_List=[]):
    Inorder_Traversal()(Tree_List[0])  # Left
    if Tree_List == None:
        return
    else:
        print(Tree_List[1])
    Inorder_Traversal(Tree_List[2])  # Right
    return Tree_List


# 后序遍历
def Postorder_Traversal(Tree_List=[]):
    Postorder_Traversal()(Tree_List[0])  # Left
    Postorder_Traversal(Tree_List[2])  # Right
    if Tree_List == None:
        return
    else:
        print(Tree_List[1])
    return Tree_List


# Common tree---
def MainNode():
    Tree = [None]
    data = input("data")
    Tree[0] = data
    while (True):
        Node = input("node")
        if Node == '`':
            return Tree
        elif Node == 'c':
            Tree.append(MainNode())


def Common_Preorder_Traversal(Tree_List=[]):
    for i in Tree_List:
        if type(i) != list:
            print(i)
        else:
            Common_Preorder_Traversal(i)


# -------------------------------------------------------------------------
# graph
# 深度优先算法
flag_graph = {}


def Depth_first_Search_Traverse(graph):
    global flag_graph
    for i in graph:
        flag_graph[i] = False
    for i in graph:
        if not flag_graph[i]:
            DFS(graph, i)


def DFS(graph, node):
    global flag_graph
    flag_graph[node] = True
    Visit(graph, node)
    w = FirstAdjVex(graph, node)
    while (True):
        if w != None:
            if not flag_graph[w]:
                DFS(graph, w)
            w = NextAdjVex(graph, node, w)
        else:
            break


def Visit(graph, node):
    print(node)


def FirstAdjVex(graph, node):
    if graph[node] == []:
        return None
    else:
        return graph[node][0]


def NextAdjVex(graph, node1, node2):
    if graph[node1].index(node2) == len(graph[node1]) - 1:
        return None
    else:
        return graph[node1][graph[node1].index(node2) + 1]


# 广度优先算法
def Breadth_first_Search(graph):
    global flag_graph
    for i in graph:
        flag_graph[i] = False
    InitQueue = []
    for i in graph:
        if not flag_graph[i]:
            flag_graph[i] = True
            Visit(graph, i)
            InitQueue.append(i)
            while InitQueue != []:
                node = InitQueue.pop(0)
                w = FirstAdjVex(graph, node)
                while (True):
                    if w != None:
                        if not flag_graph[w]:
                            flag_graph[w] = True
                            Visit(graph, w)
                            InitQueue.append(w)
                        w = NextAdjVex(graph, node, w)
                    else:
                        break


graph = {
    'v1': ['v2', 'v3'],
    'v2': ['v4'],
    'v3': ['v6', 'v7'],
    'v4': ['v8'],
    'v5': ['v2', 'v8'],
    'v6': ['v7'],
    'v7': [],
    'v8': []
}


print(Insertion_Sort([6,3,2,1]))
