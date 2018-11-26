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
def Common_Preorder_Traversal(deep,word, tree_List=[]):
    global tree_bool
    global T_bool
    this_tree_list=tree_List
    this_word = word
    if len(this_word)>1 and deep == 1:  # 当word较长,且树只有根节点时
        this_word=this_word[1:]
        tree_List.append(Common_Tree(this_word))  # 新建节点,创造树
        print('!')
        return
    if this_word == '':
        return
    for i in this_tree_list:
        if type(i) != list:  # 树中内容判断
            if i == this_word[0]:
                this_word = this_word[1:]
                print(i)
            else:
                tree_bool = True
                return
        if type(i) == list:
            Common_Preorder_Traversal(deep,this_word, i)
        if tree_bool and type(i) == list:
            i.append(Common_Tree(this_word))#新建节点,创造树
            tree_bool = False
            print(1)
            return

        # if this_word != '' and type(i) == list:#word的较长,树为完整树
        #     i.append(Common_Tree(this_word))  # 新建节点,创造树
        #     print('@')
        #     return
c=['1']
a=['1', ['2', ['3']]]
b=input()
Common_Preorder_Traversal(len(a),b,a)
print(a)
