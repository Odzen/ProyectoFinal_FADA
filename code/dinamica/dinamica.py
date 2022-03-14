import numpy as np

'''
Funcion para calcular la solucion optima del problema usando programacion
dinamica
'''

'''
Funcion principal
'''
    
def solve(n, a, b, ab, ba):
    # Declaración de variables para la salida del algoritmo (No modificar)
    #lines = []

    T,L = llenarMatrices(n, a, b, ab, ba)
        
    #n, time, lines = solucionesOptimas(T,L,n)
    time, finalLine = solucionesOptimas(T,L,n)
        
    # Salida del algoritmo (No modificar)
    #return n, time, lines
    return n, time, finalLine
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
        # Computar los valores de T[0,j] y L[0,j], fila 1 de cada array
        if T[0,j-1] +  a[j] <= T[1, j-1] + ba[j-1] + a[j]:
            T[0,j] = T[0, j-1] + a[j]
            L[0,j] = 0
        else:
            T[0,j] = T[1, j-1] + ba[j-1] + a[j]
            L[0,j] = 1
        
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
    
    # Calcular el valor de la solucion optima (time) y la linea de ensamblaje
    # en donde se termino el proceso, que sirve para calcular luego la 
    # solucion optima
    if(T[0,n-1] <= T[1,n-1]):
        time += T[0,n-1]
        finalLine=0
    else:
        time += T[1,n-1]
        finalLine=1
    
    return time,finalLine
    