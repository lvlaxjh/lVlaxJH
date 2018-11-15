from xpinyin import Pinyin
#
piny = Pinyin()
#
def Main_Shield(Input_str=''):
    #
    Input_Piny_List=[]
    #
    Input_Piny_List=Get_Shield(Input_str)
def Get_Shield(Input_str=''):
    Input_Piny_List=[]
    Input_Piny=piny.get_pinyin(Input_str,' ')
    Input_Piny_List=Input_Piny.split(' ')
    return Input_Piny_List
    # Shield_str = u'傻逼'
    # PinYList = []
    # Shield_Piny = piny.get_pinyin(Shield_str, ' ')
    # PinYList = Shield_Piny.split(' ')
    # return PinYList


str=input()
Main_Shield(str)
