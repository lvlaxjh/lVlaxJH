import ahocorasick
from xpinyin import Pinyin
import fileoperation

input_txt_all_NEW = r'txt\\libNEW.txt'
input_txt_all_OLD = r'txt\\libOLD.txt'
input_txt_pinyin = r'txt\\piyinlib.txt'
input_txt_chinese = r'txt\\wordchinese.txt'
input_txt_Initials = r'txt\\wordInitials.txt'


class Search:
    def __init__(self):
        self.__lvl_1_return_list = []
        self.__lvl_2_return_list = []
        self.__lvl_3_return_list = []
        self.__Post_processing = ''
        self.__common_tree = ahocorasick.Automaton()
        self.__pinyin_tree = ahocorasick.Automaton()
        self.__initials_tree = ahocorasick.Automaton()

    # 纯文本提取,踢出特殊字符
    def text_extraction(self, sentence):
        self.__Post_processing = ''
        for word in sentence:  # 检索文字中所有中文
            if u'\u4e00' <= word <= u'\u9fff':
                self.__Post_processing = self.__Post_processing + word
        for word in sentence:  # 检索文字中所有英文
            if u'a' <= word <= u'z':
                self.__Post_processing = self.__Post_processing + word
        for word in sentence:  # 检索文字中所有数字
            if u'0' <= word <= u'9':
                self.__Post_processing = self.__Post_processing + word

    # 创建所有DFA树
    def create_ahocorasick(self):
        idx = 1
        common_file = open(input_txt_all_NEW, 'r', encoding='UTF-8')
        pinyin_file = open(input_txt_pinyin, 'r', encoding='UTF-8')
        initials_file = open(input_txt_Initials, 'r', encoding='UTF-8')
        with  common_file as fp:
            for line in fp:
                word = line.strip()
                self.__common_tree.add_word(word, (idx, word))
                idx += 1
        idx = 1
        with  pinyin_file as fp:
            for line in fp:
                word = line.strip()
                self.__pinyin_tree.add_word(word, (idx, word))
                idx += 1
        idx = 1
        with  initials_file as fp:
            for line in fp:
                word = line.strip()
                self.__initials_tree.add_word(word, (idx, word))
                idx += 1
        idx = 1

    # lvl_1_完整句子匹配
    def level_1_search(self):
        self.__common_tree.make_automaton()
        for i in self.__common_tree.iter(self.__Post_processing):
            print(i)
            self.__lvl_1_return_list.append(i)

    # lvl_2_全拼匹配
    def level_2_search(self):
        self.__pinyin_tree.make_automaton()
        for i in self.__pinyin_tree.iter(self.__Post_processing):
            print(i)
            self.__lvl_2_return_list.append(i)
 # lvl_3_首字母匹配
    def level_3_search(self ):
        self.__initials_tree.make_automaton()
        for i in self.__initials_tree.iter(self.__Post_processing):
            print(i)
            self.__lvl_3_return_list.append(i)

sea = Search()
while (True):
    b = input()
    sea.create_ahocorasick()
    sea.text_extraction(b)
    sea.level_1_search()
    sea.level_2_search()
    sea.level_3_search()