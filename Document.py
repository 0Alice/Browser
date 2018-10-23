from PorterStemmer import PorterStemmer
import math
from nltk.corpus import stopwords

class Document:
    def __init__(self,title,originalDoc,terms,isExtension):
        self.title=title
        self.tfidf={}
        if(isExtension):
            self.originalDoc=originalDoc
        else:
            self.originalDoc=title+" "+originalDoc
        wordsList=self.stemming(self.firstStep())
        wordSet=set(wordsList)
        stopWords = set(stopwords.words('english'))
        self.wordSet = [x for x in wordSet if x not in stopWords]
        self.bagOfWords=self.createBagOfWords(wordsList,terms)
        self.finalDoc=self.createDisplayVersion(wordsList)

    def stemming(self,listOfWords):
        p = PorterStemmer()
        stemList = []
        for word in listOfWords:
            stemList.append(p.stem(word, 0, len(word) - 1))
        return stemList

    def tfidfLength(self):
        length = 0
        for _, value in self.tfidf.items():
            length += (value ** 2)
        return math.sqrt(length)

    def firstStep(self):  # pozbycie się znaków i sprowadzenie wszystkich liter do małych liter i podział na listę słów
        nextDoc=self.originalDoc.lower()
        nextDoc = nextDoc.replace("\n", '').replace(".", '').replace(",", '').replace(":", '').replace("?", '').replace(")", '').replace("(", '').replace("-", ' ').replace("/", ' ').replace("'", '').replace(">", '')
        nextDoc=nextDoc.split(' ')
        nextDoc=[i for i in nextDoc if i != '']
        return nextDoc

    def createBagOfWords(self,listOfWords, terms):
        bagOfWords = {}
        for term in terms:
            bagOfWords[term] = 0

        for word in listOfWords:
            if (word in terms):
                bagOfWords[word] += 1

        return bagOfWords

    def createDisplayVersion(self,listOfWords):
        return " ".join(listOfWords)

    def calculateTF(self,bagOfWords):
        tF = {}
        maxValue = bagOfWords[max(bagOfWords.keys(), key=(lambda k: bagOfWords[k]))]
        if(maxValue==0):
            return bagOfWords
        for key, value in bagOfWords.items():
            tF[key] = value / maxValue
        return tF

    def calculateTFIDF(self, termsIDF):
        tf = self.calculateTF(self.bagOfWords)
        tfidf = {}
        for term in termsIDF:
            tfidf[term] = tf[term] * termsIDF[term]
        self.tfidf=tfidf

