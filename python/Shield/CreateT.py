from xpinyin import Pinyin
import re

def get_terms(word):
    all_terms=[]
    if all_terms==[]:
        all_terms.append(word)
    else:
        find_same(word,all_terms)
def find_same(word,all_terms=[]):
    for i in all_terms:
        for one_in_i in range(len(i)):
            for one_in_word in range(len(word)):
                if i[one_in_i]==word[one_in_word]:
                    pass
                elif i[one_in_i]!=word[one_in_word]:
                    pass


for i in range(len([1,2,3])):
    print(len([1,2,3]))
