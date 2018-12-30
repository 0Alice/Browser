import math
from operator import itemgetter
import secrets

from PorterStemmer import PorterStemmer

from Document import Document
from Keywords import Keywords
from Centroid import Centroid


class Browser:
    def __init__(self, keywordsName, docName, isExtension, k=0, maxIterations=1):
        self.keywords = Keywords(keywordsName)

        self.docList = self.readDocs(docName, isExtension)

        self.keywords.calculateTermsIDF(self.docList)
        self.query = None
        self.similarityList = None
        for doc in self.docList:
            doc.calculateTFIDF(self.keywords.termsIDF)
        self.createCoincidenceMatrix()
        self.groups=[]
        if(k > 0):
            self.centroids = [Centroid(secrets.choice(self.docList).tfidf) for i in range(k)]
            for _ in range(maxIterations):
                if self.kNNiteration():
                    break
            for c in self.centroids:
                self.groups.append([e.title for e in c.copyOfElements])
        for g in self.groups:
            print(g)

    def kNNiteration(self):
        def argmax(iterable):
            return max(enumerate(iterable), key=lambda x: x[1])[0]
        for doc in self.docList:
            self.centroids[argmax([self.similarity(doc, centroid)
                                   for centroid in self.centroids])].elements.append(doc)
        for c in self.centroids:
            c.updateCentroid()
        return all(c.end for c in self.centroids)

    def createCoincidenceMatrix(self):
        coincidenceMatrix = {}
        for doc in self.docList:
            for w1 in doc.wordSet:
                if(w1 not in coincidenceMatrix):
                    coincidenceMatrix[w1] = {}
                for w2 in doc.wordSet:
                    if(w1 != w2):
                        if(w2 in coincidenceMatrix[w1]):
                            coincidenceMatrix[w1][w2] += 1
                        else:
                            coincidenceMatrix[w1][w2] = 1
        self.coincidenceMatrix = coincidenceMatrix

    def readDocs(self, name, isExtension):
        file = open(name)
        try:
            text = file.readlines()
        finally:
            file.close()
        emptyLine = "\n"
        singleDoc = ""
        counter = 0
        firstLine = ""
        docList = []
        for line in text:
            counter += 1
            if(line == emptyLine):
                docList.append(Document(firstLine, singleDoc,
                                        self.keywords.terms, isExtension))
                singleDoc = ""
                counter = 0
            else:
                if (counter == 1):
                    firstLine = line
                else:
                    singleDoc = singleDoc+line

        return docList

    def similarity(self, doc, query):
        sumOfSame = 0
        for key, value in query.tfidf.items():
            sumOfSame += value*doc.tfidf[key]
        if(sumOfSame == 0):
            return 0
        dl = doc.tfidfLength()
        ql = query.tfidfLength()
        if(dl == 0 or ql == 0):
            return 0
        return sumOfSame/(dl*ql)

    def documentsSimilarityList(self, queryObject):
        self.query = queryObject
        self.query.calculateTFIDF(self.keywords.termsIDF)
        similarityList = []
        for doc in self.docList:
            sim = self.similarity(doc, self.query)
            similarityList.append([doc, sim, "%.4f" % sim+"\t"+doc.title])
        self.similarityList = sorted(similarityList, key=itemgetter(1))[::-1]
