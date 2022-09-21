class Albero:
    def __init__(self,m):
        self.__m = m
        self.__radice = None
        self.__h = 0
        self.__numFoglie =0

    def getM(self):
        return self.__m

    def getRadice(self):
        return self.__radice

    def aggiungiNodo(self, nodo, padre, i):
        if padre.getNumFigli() < self.__m:
            if padre.getNumFigli()!=0:
                self.__numFoglie+=1
            padre.aggiungiFiglio(i,nodo)
            nodo.setPadre(padre)
            l = nodo.getLivello()
            print('Aggiunto nodo: ',nodo.getInfo(),'Livello: ',l)
            if self.__h < l:
                self.__h = l
            self.__numFoglie+=nodo.getNumFoglie()
            return True
        return False

    def aggiungiRadice(self, radice):
        if self.__radice == None:
            self.__radice = radice
            self.__numFoglie+=1
        else:
            r = self.__radice
            r.setPadre(radice)
            self.__radice=radice
            self.__radice.aggiungiFiglio(0,r)
        self.__h += 1

    def getAltezza(self):
        return self.__h


    def visitaProfondita(self, nodo, listaInfo):
        if nodo != None:
            listaInfo.append(nodo.getInfo())
            figli = nodo.getFigli()
            for f in figli:
                self.visitaProfondita(f, listaInfo)

    def visitaAmpiezza (self, nodo):
        info = []
        lista = [nodo]
        while len(lista)>0:
            r = lista.pop(0)
            lista.extend(r.getFigli())
            info.append(r.getInfo())
        return info

    def getNumFoglie(self):
        return self.__numFoglie

    def getNumNodiInterni(self,nodo):
        return nodo.getNumNodiInterni()
