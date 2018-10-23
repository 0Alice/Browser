from collections import Counter
from Document import Document

class Query(Document) :
    def __init__(self,query,terms,isExtension):
        Document.__init__(self,"",query,terms,isExtension)
        self.extension=[]

    def getExtesion(self,coincidenceMatrix):
        allCoincidenceWords={}
        #TODO when word is not in coincidenceMatrix
        for key in self.wordSet:
            allCoincidenceWords={ k: allCoincidenceWords.get(k, 0) + coincidenceMatrix[key].get(k, 0) for k in set(allCoincidenceWords) | set(coincidenceMatrix[key])}
        for key in self.wordSet:
            allCoincidenceWords[key]=0
        #print(dict(Counter(allCoincidenceWords).most_common(10)))
        for key,value in dict(Counter(allCoincidenceWords).most_common(10)).items():
            self.extension.append(key+"\t"+str(value))
        print(self.extension)
        #{ k: x.get(k, 0) + y.get(k, 0) for k in set(x) | set(y) }
        #print(dict(Counter(coincidenceMatrix[list(self.wordSet)[0]]).most_common(10)))
        '''shorterMatrix={}
        for word, coincidenceWords in coincidenceMatrix.items():
            shorterMatrix[word]=dict(Counter(coincidenceWords).most_common(10))'''
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