import ahocorasick


class Search:
    def __init__(self):
        self.__allbadword='badwordlib.txt'
        self.__lvl_1_return_list=[]
    def level_1_search(self,sentence):
        wordtree = ahocorasick.Automaton()
        badwordfile=open(self.__allbadword, 'r',encoding='UTF-8')
        with  badwordfile as fp:
            for line in fp:
                word = line.strip()
                wordtree.add_word(word, (1, word))
        print(type(wordtree))
        wordtree.make_automaton()
        # print(list(wordtree.keys()))
        for i in wordtree.iter(sentence):
            print(i)
            self.__lvl_1_return_list.append(i)
    def level_2_search(self):
        print(self.__lvl_1_return_list)
def word_retrieval():
    badwordtxt = 'allword.txt'
    inputtxt='badwordlib.txt'
    wordtree = ahocorasick.Automaton()
    with open(badwordtxt, 'r', encoding='UTF-8') as fp:
        for line in fp:
            word = line.strip()
            wordtree.add_word(word, (10, word))
    print(type(wordtree))
    wordtree.make_automaton()
    wordlist=list(wordtree.keys())
    for i in wordlist:
        print(i)
    inputt=open(inputtxt, 'w', encoding='UTF-8')
    for i in wordlist:
        inputt.writelines(i+'\n')

# input_badword()
a=Search()
while(True):
    b=input()
    a.level_1_search(b)
    a.level_2_search()

