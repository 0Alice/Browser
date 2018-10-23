from Document import Document
from Keywords import Keywords
from operator import itemgetter
import math
from PorterStemmer import PorterStemmer


class Browser:
    def __init__(self,keywordsName,docName,isExtension):
        self.keywords=Keywords(keywordsName)

        self.docList=self.readDocs(docName,isExtension) #stworzenie dokumentu

        self.keywords.calculateTermsIDF(self.docList)
        self.query = None
        self.similarityList=None
        for doc in self.docList:
            doc.calculateTFIDF(self.keywords.termsIDF)
        self.createCoincidenceMatrix()

    def createCoincidenceMatrix(self):
        coincidenceMatrix={}
        for doc in self.docList:
            for w1 in doc.wordSet:
                if(w1 not in coincidenceMatrix):
                    coincidenceMatrix[w1]={}
                for w2 in doc.wordSet:
                    if(w1!=w2):
                        if(w2 in coincidenceMatrix[w1]):
                            coincidenceMatrix[w1][w2]+=1
                        else:
                            coincidenceMatrix[w1][w2]=1
        self.coincidenceMatrix=coincidenceMatrix

    def readDocs(self,name,isExtension):
        file = open(name)
        try:
            text = file.readlines()
        finally:
            file.close()
        emptyLine="\n"
        singleDoc=""
        counter=0
        firstLine=""
        docList=[]
        for line in text:
            counter+=1
            if(line==emptyLine):
                docList.append(Document(firstLine,singleDoc,self.keywords.terms,isExtension))
                singleDoc=""
                counter=0
            else:
                if (counter == 1):
                    firstLine = line
                else:
                    singleDoc=singleDoc+line


        return docList

    def similarity(self,doc):
        sumOfSame=0
        for key, value in self.query.tfidf.items():
            sumOfSame+=value*doc.tfidf[key]
        if(sumOfSame==0):
            return 0
        dl=doc.tfidfLength()
        ql=self.query.tfidfLength()
        if(dl==0 or ql==0):
            return 0
        return sumOfSame/(dl*ql)

    def documentsSimilarityList(self,queryObject):
        self.query=queryObject
        self.query.calculateTFIDF(self.keywords.termsIDF)
        similarityList=[]
        for doc in self.docList:
            sim=self.similarity(doc)
            similarityList.append([doc,sim,"%.4f" % sim+"\t"+doc.title])
        self.similarityList=sorted(similarityList, key=itemgetter(1))[::-1]