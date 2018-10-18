from textblob import Word
from textblob.wordnet import VERB
from nltk.corpus import wordnet as wn


class Query :
    def __init__(self,query):
        self.query=Word(query)
        self.findExtensions()




    def findExtensions(self):
        print("lllllll")
        word=wn.synsets('dog')
        print(word)
        set=wn.synset('dog.n.01')
        print("setttttt")
        print(set)
        print("holo")
        holo = set.member_holonyms()
        print(holo)
        print("mero")
        mero=set.part_meronyms()
        print(mero)



        print("cccccc")
        for a in mero:
            print("in")
            print("el "+a.name())
            print("def "+a.definition())