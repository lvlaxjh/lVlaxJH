from xpinyin import Pinyin
import re


# Input_Piny = piny.get_pinyin(Input_str, ' ')


def Create_SWT():
    ShieldWordTree = []
    while(True):
        word=input('input--->')
        if word=='`':#退出
            break
        if ShieldWordTree!=[]:
            for i in ShieldWordTree:
                Common_Preorder_Traversal(word,i)
        ShieldWordTree.append(Common_Tree(word))
    return ShieldWordTree

def Common_Tree(word):
    this_word=word
    tree=[]
    tree.append(this_word[0])
    this_word=this_word[1:]
    if this_word=='':#写入完成
        return tree
    tree.append(Common_Tree(this_word))
    return tree

tree_bool=False
T_bool=False
def Common_Preorder_Traversal(word,tree_List=[]):
    global tree_bool
    global T_bool
    this_word=word
    if this_word=='':
        return
    for i in tree_List:
        if type(i)!=list:#树中内容判断
            if i==this_word[0]:
                this_word=this_word[1:]
                print(i)
                T_bool=True
            else:
                T_bool = False
                tree_bool=True
                return False
        if type(i)==list:
            Common_Preorder_Traversal(this_word,i)
        if tree_bool:
            #i.append(Common_Tree(this_word))#新建节点,创造树
            tree_bool=False
            print(1)

Create_SWT()