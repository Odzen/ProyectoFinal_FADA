import numpy as np

'''
Funcion para calcular la solucion optima del problema usando programacion
dinamica
'''

'''
Funcion principal
'''
    
def solve(n, a, b, ab, ba):
    # Declaraci�n de variables para la salida del algoritmo (No modificar)
    #lines = []

    T,L = llenarMatrices(n, a, b, ab, ba)
        
    #n, time, lines = solucionesOptimas(T,L,n)
    time, lines = solucionesOptimas(T,L,n)
        
    # Salida del algoritmo (No modificar)
    #return n, time, lines
    return n, time, lines
    #return  T,L


'''
Funciones auxiliares
'''

## Funcion auxiliar para llenar las matrices T y L
## T -> Matriz que guardara los valores de la solucion optima (time) para cada subproblema
## L -> Matriz aux que guardara los valores de la linea de ensamblaje que se escoge
## en cada subproblema, a partir de L calcularemos la solucion optima

def llenarMatrices(n, a, b, ab, ba):

    # Algoritmo con dinamica
    # Array para guardar el valor de la solucion optima en terminos de tiempo
    T = np.zeros([2, n], dtype = int)
    
    # Array para guardar la matriz auxiliar de la solucion optima, de la cual
    # luego se calcula la solucion optima
    L = np.zeros([2, n], dtype = int)

    # Casos base, cuando se analiza la actividad 1
    # Recordar que por facilidad, indexamos empezando 0
    T[0,0] = a[0]
    T[1,0] = b[0]
    
    L[0,0] = 0
    L[1,0] = 1

    # Ciclo for de 1 hasta n sin incluirlo, iterando de a 1
    # Populando matriz de valor de solucion optima y matriz auxiliar
    for j in range(1,n):
        #print("Actividad #: ", j)
        #print(ab[j-1])
        #print("Linea 1")
        #print("Por a: ", T[0,j-1] , "+",  a[j] , "=", ) 
        #print("Por b: ", T[1, j-1] + ba[j-1] + a[j])
        # Computar los valores de T[0,j] y L[0,j], fila 1 de cada array
        if T[0,j-1] +  a[j] <= T[1, j-1] + ba[j-1] + a[j]:
            T[0,j] = T[0, j-1] + a[j]
            L[0,j] = 0
        else:
            T[0,j] = T[1, j-1] + ba[j-1] + a[j]
            L[0,j] = 1
        
        
        #print("Linea 2")
        #print("Por b: ", T[1,j-1] +  b[j])
        #print("Por a: ", T[0, j-1] + ab[j-1] + b[j])
        
        # Computar los valores de T[1,j] y L[1,j], fila 2 de cada array
        if T[1,j-1] +  b[j] <= T[0, j-1] + ab[j-1] + b[j]:
            T[1,j] = T[1,j-1] +  b[j]
            L[1,j] = 1
        else:
            T[1,j] = T[0, j-1] + ab[j-1] + b[j]
            L[1,j] = 0

    return T,L


## Funcion auxiliar solucionesOptimas: 
## Calcula a partir de las matrices el valor de la solucion optima -> Tiempo total
#  y la solucion optima -> Secuencia de lineas de ensamblaje

def solucionesOptimas(T,L,n):
    
    time = 0
    finalLine = ' '
    lines=[]
    
    # Calcular el valor de la solucion optima (time) y la linea de ensamblaje
    # en donde se termino el proceso, que sirve para calcular luego la 
    # solucion optima
    if(T[0,n-1] <= T[1,n-1]):
        time += T[0,n-1]
        finalLine=0
    else:
        time += T[1,n-1]
        finalLine=1
    
    ## Calcular el camino que se escogio para lograr el tiempo minimo
    ## Con un for que va desde n-1 hasta 0 incluyendolo
    lines.append(finalLine)
    
    for j in range(n-1,-1,-1):
        # Saltarse la l�nea n-1, puesto que la necesitamos solo para refereciar
        # no para alamacenar, no hace parte de la solucion optima
        #print(finalLine, j) 
        if(j==n-1):
            #print("Entro")
            finalLine = L[finalLine][j]
        else:
            finalLine = L[finalLine][j]
            lines.append(finalLine)   
          
    # revertir la lista puesto que nos arroja el camino del ultimo punto
    # al primero (fin->inicio), y queremos el camino del primer punto
    # al ultimo (inicio -> fin)
    lines=list(reversed(lines))
    
    # Se llama la funcion auxiliar tranformAB para dar la salida en el formato
    # requerido
    lines=transformAB(lines)
    
    return time,lines


#Funcion auxiliartransformAB, tranform Transformar 0 -> 'a' y 1-> 'b' para lines

def transformAB(lines):
    linesAux=[]
    for line in lines:
        if(line == 1):
            linesAux.append('b')
        else:
            linesAux.append('a')
    return linesAux
    