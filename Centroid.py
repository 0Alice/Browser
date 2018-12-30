from Document import Document

class Centroid(Document) :
    def __init__(self,tfidf):
        Document.__init__(self,"","","",False)
        self.tfidf=tfidf
        self.elements=[]
        self.copyOfElements=[]
        self.end=False

    def updateCentroid(self):
        if(self.copyOfElements==self.elements):#TODO check if it works
            self.end=True
        else:
            self.end=False
            self.updateTFIDF()
        self.copyElements()

    def updateTFIDF(self):
        tfidf={}
        for e in self.elements:
            for key, value in e.tfidf.items():
                if(key not in tfidf):
                    tfidf[key] = value
                else:
                    tfidf[key] += value
        numOfElements=len(self.elements)
        for key, value in tfidf.items():
            tfidf[key] = value/numOfElements
        self.tfidf=tfidf

    def copyElements(self):
        self.copyOfElements=self.elements.copy()
        self.elements=[]