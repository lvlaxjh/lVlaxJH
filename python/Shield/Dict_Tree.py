from xpinyin import Pinyin

tree_dict={
            '阿':{
                'child':{
                    '扁':{
                        'child':{
                            '推':{
                                'child':{
                                    '翻':{
                                        'child':{None},
                                        'word':'阿扁推翻'
                                    }
                                }
                            }
                        }
                    },
                    '宾':{
                        'child':{None},
                        'word':'阿宾'
                    },
                    '賓':{
                        'child':{None},
                        'word':'阿賓'
                    }
                }
            },
            '挨':{
                'child':{
                    '了':{
                        'child':{
                            '一':{
                                'child':{
                                    '炮':{
                                        'child':{None},
                                        'word':'挨了一炮'
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
class Node(object):
    def __init__(self):
        self.child=None
        self.badword=None

def add_word_in_dict(root,word):
    node=root
    for i in range(len(word)):
        if node.child==None:
            node.child={}
            node.child[word[i]]=Node()
        elif word[i] not in node.child:
            node.child[word[i]]=Node()
        node=node.child[word[i]]
    node.badword=word

a={'1':{None}}
if a['1']=={None}:
    print(type(a['1']))