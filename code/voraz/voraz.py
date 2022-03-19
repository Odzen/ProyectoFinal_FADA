##import numpy as np

'''
Función donde deben introducir la lógica de su algoritmo. Pueden declarar
variables globales si lo consideran conveniente.
'''


def solve(n, a, b, ab, ba):
   
    matriz_ = matriz(a,b,ab,ba)

    # Declaración de variables para la salida del algoritmo (No modificar)
    time , lines = voraz(a,b,matriz_)

    # Algoritmo con voraz
    
    # Fin del algoritmo

    # Salida del algoritmo (No modificar)
    return n, time, lines

  ##  /*Indica la actividad  por la cual se empieza
   

def verticeInicio (a,b):

    vertice = 0  

    if (a[0]<b[0]):
            vertice=a[0]
    else:
            vertice=b[0]
    
    return vertice


def minimo(a):

    minimo = a[0]

    for j in range(1,len(a)):
         if minimo > a [j]:
             minimo = a[j]

    return minimo          

def salidaRuta (r):

    ruta = []
     
    for j in range(0,len(r)):
         if r[j]<len(r):
             ruta.append("a")
         else:
                 ruta.append("b")
    return ruta

def matriz (a,b,ab,ba):

    completo = []
    for j in range(0,len(a)):
         completo.append(a[j])

    for i in range(0,len(b)):
         completo.append(b[i])
    
    ##print(completo)

    matriz = []
    for i in range (len(completo)):
        matriz.append([0]*len(completo))

   ## print(matriz)
    
    mitad = int(len(completo)/2)
    
    ultimo =len(completo)-1
    contador1 = 0
    contador2 = mitad+1
    
    contador3=0
    
    for x in range(0,len(a)):   
         contador1 = x+1
         for y in range(0,len(completo)):    
              if x == mitad:
                  matriz [x][y]=999
              elif y == contador1:
                  matriz [x][y]=completo[y]
              elif y == contador2:
                  matriz [x][y] = completo[y]+ab[contador3]
                  contador3 = contador3 + 1
              else:
                  matriz [x][y]=999
    
         contador2 = contador2 + 1
       
   
    contador2=mitad+1 
    contador3=0
    contador1=0

    for x2 in range(mitad,len(completo)):   
        contador1 = contador1+1
        for y2 in range(0,len(completo)):    
              if x2 == ultimo:
                  matriz [x2][y2]=999
              elif y2 == contador1:
                  matriz [x2][y2]=completo[y2]+ba[contador3]
                  contador3 = contador3 + 1
              elif y2 == contador2:
                  matriz [x2][y2]=completo[y2]
                  contador3 + 1
              else:
                  matriz [x2][y2]=999
                  
        contador2 = contador2+1
        
    return matriz

def voraz (a,b,matriz):

    iteracion=0
    inicia = verticeInicio(a,b)
    tiempoTotalM = inicia
    ruta = [] 
    solucion = []
    verticesCambio = [] 
    vertices = []
    c = []

    for x in range(0,len(a)):
         c.append(a[x])

    for i in range(0,len(a)):
         c.append(b[i])

    for l in range(0,len(c)):
         verticesCambio.append(l)
         vertices.append(l)

    division = int((len(verticesCambio)/2)-1)

    if inicia == b[iteracion]:
        posicionInicia = int(b.index(inicia) + int(len(verticesCambio)/2))
        verticesCambio.remove(verticesCambio[posicionInicia])
        verticesCambio.remove(verticesCambio[0])
    else:
        posicionInicia = a.index(inicia)
        verticesCambio.remove(verticesCambio[posicionInicia])
        verticesCambio.remove(verticesCambio[division])
    print(posicionInicia)
    print(verticesCambio)
    
    ruta.append(posicionInicia)
    '''
    if posicionInicia>division:
        verticesCambio.remove(verticesCambio[posicionInicia])
        verticesCambio.remove(verticesCambio[0])
    else:
        verticesCambio.remove(verticesCambio[posicionInicia])
        verticesCambio.remove(verticesCambio[division])
    '''
    print (len(verticesCambio))
    
    while bool(verticesCambio):

        pv=posicionInicia

        for i in range (0,len(c)):
            solucion.append(matriz[pv][i])
            
        print (solucion)   
    
        tiempoTotalM = tiempoTotalM + minimo(solucion)

       
        c_ = solucion.index(minimo(solucion))
        print(verticesCambio)
        print(c_)
        e = verticesCambio.index(vertices[c_])
        print(e)
      
        ruta.append(c_)
        
        division = int((len(verticesCambio)/2)-1)
        print(division)
        print(len(verticesCambio))
        
        if c_>division:
            verticesCambio.remove(verticesCambio[e])
            verticesCambio.remove(verticesCambio[0])
        else:
            verticesCambio.remove(verticesCambio[e])
            verticesCambio.remove(verticesCambio[division])

        posicionInicia=c_

        for i in range(0,len(solucion)):
            solucion.pop(0)
        
    
      
    print(verticesCambio)
    
    return tiempoTotalM,salidaRuta(ruta)