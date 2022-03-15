import numpy as np
import random

"""
Creacion de test automatico
"""
nombreEscritura="in"

def test_creation(n, numeroTest):
    
    #Cotas entre las cuales se escogerá el número random para a y b
    cotaMenor=1
    cotaMayor=30
    
    #Cotas mayor para ab y ba
    cotaMayorABBA=int(30/2)
    
    
    a = np.zeros([n], dtype = int)
    b = np.zeros([n], dtype = int)
    ab = np.zeros([n-1], dtype = int)
    ba = np.zeros([n-1], dtype = int)
    
    for i in range(n):
        numeroRandom=random.randint(cotaMenor, cotaMayor)
        a[i] = numeroRandom
        numeroRandom=random.randint(cotaMenor, cotaMayor)
        b[i] = numeroRandom
    for i in range(n-1):
        numeroRandom=random.randint(cotaMenor, cotaMayorABBA)
        ab[i] = numeroRandom
        numeroRandom=random.randint(cotaMenor, cotaMayorABBA)
        ba[i] = numeroRandom
        
    output= n, a, b, ab, ba
    
    outputForTest(output, numeroTest)
        
    return output;


def outputForTest(output, numeroTest):
    n, a, b, ab, ba = output
    toWrite = ""
    toWriteA=""
    toWriteB=""
    toWriteAB=""
    toWriteBA=""
    toWrite += str(n) + "\n"
    
    for element in a:
        toWriteA += " "+str(element) 
        toWriteA=toWriteA.lstrip()
    toWrite+=toWriteA+"\n"
    
    for element in b:
        toWriteB += " "+str(element) 
        toWriteB=toWriteB.lstrip()
    toWrite+=toWriteB+"\n"
    
    for element in ab:
        toWriteAB += " "+str(element) 
        toWriteAB=toWriteAB.lstrip()
    toWrite+=toWriteAB+"\n"
    
    for element in ba:
        toWriteBA += " "+str(element) 
        toWriteBA=toWriteBA.lstrip()
    toWrite+=toWriteBA+"\n"

    with open("../Pruebas/Tests_in_files/"+nombreEscritura+numeroTest+".txt", "w") as f:
        f.write(toWrite)


# Llamo funcion principal para la creacion del test
test_creation(6, "6")
test_creation(30, "7")
test_creation(50, "8")
test_creation(100, "9")