from Albero_m_ario import Albero
from Nodo_m_ario import Nodo_m_ario


#main
t = Albero(3)
listainfo = []
listanodi = []
listanodi.append(Nodo_m_ario('A'))
listanodi.append(Nodo_m_ario('B'))
listanodi.append(Nodo_m_ario('C'))
listanodi.append(Nodo_m_ario('D'))
listanodi.append(Nodo_m_ario('E'))
listanodi.append(Nodo_m_ario('F'))
listanodi.append(Nodo_m_ario('G'))
listanodi.append(Nodo_m_ario('H'))
listanodi.append(Nodo_m_ario('I'))
listanodi.append(Nodo_m_ario('L'))
listanodi.append(Nodo_m_ario('M'))

t.aggiungiRadice(listanodi[0])
for i in range(1,4):
    t.aggiungiNodo(listanodi[i], listanodi[0],i-1)

t.aggiungiNodo(listanodi[4], listanodi[1],0)
t.aggiungiNodo(listanodi[5], listanodi[1],1)
t.aggiungiNodo(listanodi[6], listanodi[2],0)
t.aggiungiNodo(listanodi[7], listanodi[3],0)
t.aggiungiNodo(listanodi[8], listanodi[3],1)
t.aggiungiNodo(listanodi[9], listanodi[3],2)
t.aggiungiNodo(listanodi[10], listanodi[7],0)

t.visitaProfondita(listanodi[0], listainfo)
print(listainfo)

listaprova = []
listaprova = t.visitaAmpiezza(listanodi[0])
print(listaprova)

figli = listanodi[0].getFigli()
for n in figli:
    print(n.getInfo())

altezza = t.getAltezza()
print(altezza)

numFoglie = t.getNumFoglie()
print(numFoglie)

n = Nodo_m_ario('N')
t.aggiungiRadice(n)

listainfo=[]
t.visitaProfondita(n, listainfo)
print(listainfo)

altezza = t.getAltezza()
print(altezza)

nodiInterni = t.getNumNodiInterni(n)
print(nodiInterni)











