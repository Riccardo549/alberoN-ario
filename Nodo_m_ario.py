class Nodo_m_ario:
    def __init__(self,info):
        self.__info = info #info string
        self.__padre = None
        self.__figli= []

    def getNumFigli(self):
        return len(self.__figli)

    def aggiungiFiglio(self, i, figlio):
        i = i%(len(self.__figli)+1)
        self.__figli.insert(i,figlio)

    def getNumFoglie(self):
        if len(self.__figli) == 0:
            return 0
        s=0
        for f in self.__figli:
            s = s+f.getNumFoglie()
        return s

    def getInfo(self):
        return self.__info


    def getFigli(self):
        return self.__figli

    def getPadre(self):
        return self.__padre

    def setPadre(self, padre):
        self.__padre = padre

    def getNumNodiInterni(self):
        if len(self.__figli) == 0:
            return 0
        s=1
        for f in self.__figli:
            s = s+f.getNumNodiInterni()
        return s

    def numeroFigliInterni(self):
        s=0
        if self.getNumFigli() > 0:
            for f in self.getFigli():
                if f.getNumFigli()>0:
                    s+=1
        else:
            s = -1 #se il nodo è foglia ritorna -1
        return s

    def getInfoFigliInterni(self):
        s = []
        if self.getNumFigli() > 0:
            for f in self.getFigli():
                if f.getNumFigli() > 0:
                    s.append(f.getInfo())
        return s


    def setInfo(self, info):
        if self.getNumFigli()>0:
            self.__info= info
            return True
        return False

    def getPadreNodoInterno(self):
        if self.getNumFigli()>0:
            return self.__padre,True
        return self.__padre,False

    def getLivello(self):
        l = 0
        nodo = self.__padre
        while nodo != None:
            l += 1
            nodo = nodo.getPadre()
        return l
