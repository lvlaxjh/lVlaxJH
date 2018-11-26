from xpinyin import Pinyin
import re


# Input_Piny = piny.get_pinyin(Input_str, ' ')


def Create_SWT():
    ShieldWordTree = []
    while (True):
        word = input('input--->')
        if word == '`':  # 退出
            break
        # if ShieldWordTree != []:
        #     for i in ShieldWordTree:
        #         Common_Preorder_Traversal(len(i),word, i)
        ShieldWordTree.append(Common_Tree(word))
    return ShieldWordTree


def Common_Tree(word):
    this_word = word
    tree = []
    tree.append(this_word[0])
    this_word = this_word[1:]
    if this_word == '':  # 写入完成
        return tree
    tree.append(Common_Tree(this_word))
    return tree


tree_bool = False
T_bool = False

#情况:
#1.word短,不同->v
#2.word相等长,不同->v
#3.word相等长,相同->v
#4.word长,基础部分不同->v
#5.word长,基础部分相同
# tree_deep=0
# def find_deep(tree_List=[]):
#     tree_deep+=1
#     if len(tree_List)==1:
#         return tree_deep
#     elif len(tree_List)==2:
#         find_deep(tree_List)
word_shield=False
def Common_Preorder_Traversal(word, tree_List=[]):
    global  word_shield
    this_word=word
    this_tree_list=tree_List
    for i in this_tree_list:
        if type(i) !=list:#为数据段
            if i ==this_word[0]:
                this_word=this_word[1:]
            else:#文字不匹配
                word_shield=True
                return this_word
        if type(i)==list:#为节点,进行递归
            Common_Preorder_Traversal(this_word,i)
        if type(i)==list and len(i)==1 and len(this_word)>1:#word较长,且基础部分相同
            i.append(Common_Tree(this_word[1:]))
            return
        if this_word=='':
            return this_word
        # if word_shield and type(i)==list and len(i)==1:
        #     return
        if word_shield and type(i)==list:#新建树节点,将不匹配内容写入树中
            this_tree_list.append(Common_Tree(this_word))
            word_shield=False
            return





c=['1']
a=['1', ['2', ['3']]]
e=['1', ['2']]
b=input()
Common_Preorder_Traversal(b,a)
print(a)

#1234
#1245