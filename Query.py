from collections import Counter

from Document import Document

class Query(Document) :
    def __init__(self,query,terms,isExtension):
        Document.__init__(self,"",query,terms,isExtension)
        self.extension=[]

    def getExtesion(self,coincidenceMatrix):
        allCoincidenceWords={}
        for key in self.wordSet:
            if(key in coincidenceMatrix):
                allCoincidenceWords={ k: allCoincidenceWords.get(k, 0) + coincidenceMatrix[key].get(k, 0) for k in set(allCoincidenceWords) | set(coincidenceMatrix[key])}
        for key in self.wordSet:
            if(key in coincidenceMatrix):
                allCoincidenceWords[key]=0

        for key,value in dict(Counter(allCoincidenceWords).most_common(10)).items():
            self.extension.append([key,str(value),key+"\t"+str(value)])
        print(self.extension)
        
'''
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





        print("cccccc")
        for a in mero:
            print("in")
            print("el "+a.name())
            print("def "+a.definition()
'''