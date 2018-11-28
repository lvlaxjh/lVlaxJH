import ahocorasick
from xpinyin import Pinyin

input_txt_all_NEW = r'txt\\libNEW.txt'
input_txt_all_OLD = r'txt\\libOLD.txt'
input_txt_pinyin = r'txt\\piyinlib.txt'
input_txt_chinese = r'txt\\wordchinese.txt'
input_txt_Initials = r'txt\\wordInitials.txt'


# 首字母提取
def get_Initials():
    piny = Pinyin()
    input_file=open(input_txt_chinese, 'r', encoding='UTF-8')
    output_file=open(input_txt_Initials, 'w', encoding='UTF-8')
    with input_file as fp:
        for line in fp:
            initials=''
            wordline = line.strip()
            for i in wordline:
                get_Piny = piny.get_pinyin(i, '')
                initials=initials+get_Piny[0:1]
            if len(initials)>1:
                output_file.writelines(initials + '\n')

# 提取中文关键词
def find_chinese():
    flag = False
    input_file = open(input_txt_all_NEW, 'r', encoding='UTF-8')
    output_cn = open(input_txt_chinese, 'w', encoding='UTF-8')
    with input_file as fp:
        for line in fp:
            wordline = line.strip()
            for i in wordline:
                if u'\u4e00' <= i <= u'\u9fff':
                    flag = True
            if flag:
                output_cn.writelines(wordline + '\n')
                flag = False


# 对重复词语删选
def word_retrieval():
    wordtree = ahocorasick.Automaton()
    with open(input_txt_all_OLD, 'r', encoding='UTF-8') as fp:
        for line in fp:
            word = line.strip()
            wordtree.add_word(word, (10, word))
    wordtree.make_automaton()
    wordlist = list(wordtree.keys())
    inputt = open(input_txt_all_NEW, 'w', encoding='UTF-8')
    for i in wordlist:
        inputt.writelines(i + '\n')


# 文本转全拼拼音
def word_to_pinyin():
    piny = Pinyin()
    input_file = open(input_txt_all_NEW, 'r', encoding='UTF-8')
    output_pinyin = open(input_txt_pinyin, 'w', encoding='UTF-8')
    with input_file as fp:
        for line in fp:
            wordline = line.strip()
            get_Piny = piny.get_pinyin(wordline, '')
            output_pinyin.writelines(get_Piny + '\n')


def operating():
    print('->')
    word_retrieval()
    print('查重->完成')
    word_to_pinyin()
    print('转拼音->完成')
    find_chinese()
    print('提取全中文->完成')
    get_Initials()
    print('首字母提取->完成')

