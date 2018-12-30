from collections import Counter
from nltk.corpus import wordnet as wn

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
        self.extension=[]
        if(not bool(allCoincidenceWords)):
            for query in self.wordSet:
                synset=wn.synsets(query)
                for synonyms in synset:
                    for key in synonyms.lemmas():
                        if(key.name()!=query):
                            self.extension.append([key.name(),0,key.name()+"\t0"])
        else:
            for key,value in dict(Counter(allCoincidenceWords).most_common(10)).items():
                self.extension.append([key,value,key+"\t"+str(value)])