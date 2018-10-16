import math
from PorterStemmer import PorterStemmer


class Keywords:
    def __init__(self,fileName):
        self.terms=self.stemming(self.readFile(fileName))
        self.termsIDF={}

    def stemming(self,listOfWords):
        p = PorterStemmer()
        stemList = []
        for word in listOfWords:
            stemList.append(p.stem(word, 0, len(word) - 1))
        return stemList

    def readFile(self,name):
        #'C:\\Users\\Ania\\Desktop\\keywords.txt'
        file = open(name)
        try:
            text = file.readlines()
        finally:
            file.close()
        keywords=[]
        for line in text:
            keywords.append(line.split('\n')[0])
        return keywords

    def calculateTermsIDF(self,documents):
        termsCount={}
        for term in self.terms:
            termsCount[term]=0
            for document in documents:
                if document.bagOfWords[term]>0:
                    termsCount[term]+=1
        idf={}
        documentsSize=len(documents)
        for key, value in termsCount.items():
            if value==0:
                idf[key]=0
            else:
                idf[key]=math.log(documentsSize/value)
        self.termsIDF=idf