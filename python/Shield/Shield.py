from xpinyin import Pinyin
import re


# Input_Piny = piny.get_pinyin(Input_str, ' ')


def Create_SWT():
    ShieldWordTree = []
    while (True):
        word = input()
        if word == '`':
            break
        if ShieldWordTree!=[]:
            Traversal(word, ShieldWordTree)
        ShieldWordTree.append(Common_Tree(word))
        print(ShieldWordTree)

    return ShieldWordTree


def Common_Tree(Word):
    this_Word = Word
    Tree = [None]
    if this_Word == '':
        return Tree
    Tree[0] = Word[0]
    this_Word = this_Word[1:]
    Tree.append(Common_Tree(this_Word))
    return Tree


def Traversal(word,ShieldWordTree=[]):
    for i in ShieldWordTree:
        Common_Preorder_Traversal(word,i)


def Common_Preorder_Traversal(word,Tree_List=[]):
    this_word=word
    if this_word=='':
        return
    for i in Tree_List:
        if i==None and this_word!='':
            print(this_word)
        if type(i) != list:
            if this_word[0]==i:
                print(i)
                this_word=this_word[1:]
            # else:#树中插入节点

                # Common_Tree(word)
                # return
        else:
            Common_Preorder_Traversal(this_word,i)


All_World_List = Create_SWT()

