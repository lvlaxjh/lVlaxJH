from xpinyin import Pinyin
import re
#Input_Piny = piny.get_pinyin(Input_str, ' ')
ShieldWordTree=[]
def CreateSWT():
    Word=input()
    Word_List=[]
    for i in Word:
        Word_List.append(i)
    i=0
    ShieldWordTree.append(Create_Tree(i,Word_List))
    print(ShieldWordTree)
def Create_Tree(i,WordL=[]):
    Tree = [None]#创建树节点
    Tree[0] = WordL[i]#节点0为数据位置
    i+=1
    if i<len(WordL):
        Tree.append(Create_Tree(i,WordL))
    return Tree




CreateSWT()