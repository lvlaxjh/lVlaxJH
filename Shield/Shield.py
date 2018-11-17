from xpinyin import Pinyin
import re

#
piny = Pinyin()


#
def Main_Shield(Input_str=''):
    #
    Input_Piny_List = []
    #
    Input_Piny_List = Get_Input_Piny(Input_str)
    print(Input_Piny_List)


def Get_Input_Piny(Input_str=''):
    # IsChinese=re.compile()
    GetStr = ''
    for i in Input_str:
        FindCHinese = re.search(u'[\u4e00-\u9fa5]+', i)
        FindEnglish_or_Number = re.search('[a-zA-Z0-9]', i, re.I)
        if FindCHinese:#中文
            GetStr = GetStr + i
        elif FindEnglish_or_Number:#英文\数字
            GetStr = GetStr + i
    Input_str=GetStr
    Input_Piny_List = []
    Input_Piny = piny.get_pinyin(Input_str, ' ')
    Input_Piny_List = Input_Piny.split(' ')
    return Input_Piny_List


def Shield(Input_Piny_List=[]):
    pass


str = input()
Main_Shield(str)
