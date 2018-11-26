from xpinyin import Pinyin
import re


# Input_Piny = piny.get_pinyin(Input_str, ' ')


def Create_SWT():
    ShieldWordTree = []
    while (True):
        word = input('input--->')
        if word == '`':  # 退出
            break
        if ShieldWordTree==[]:
            ShieldWordTree.append(Common_Tree(word))#若树为空,直接加入元素
        else:
            for i in ShieldWordTree:#遍历所有根节点
                if word[0]!=i[0]:#若一个根节点不同,直接创建新节点
                    ShieldWordTree.append(Common_Tree(word))
                else:
                    Common_Preorder_Traversal(word,i)#否则,进入比较创建树
        print(ShieldWordTree)#--->打印树
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


test1=[['1', ['2', ['3']], ['3', ['4']]]]

a=input()
Common_Preorder_Traversal(a,test1)
# Create_SWT()