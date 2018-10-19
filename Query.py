from textblob import Word
from textblob.wordnet import VERB
from nltk.corpus import wordnet as wn


class Query :
    def __init__(self,query):
        self.query=wn.synsets(query)[0]
        self.findExtensions()




    def findExtensions(self):
        holonyms=self.query.member_holonyms()
        print(holonyms)
        meronyms=self.query.part_meronyms()
        print(meronyms)





    '''print("cccccc")
        for a in mero:
            print("in")
            print("el "+a.name())
            print("def "+a.definition()'''