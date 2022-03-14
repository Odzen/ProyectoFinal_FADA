'''
Funcion para calcular la solucion optima del problema usando programacion
dinamica
'''
## Funcion principal
def solve(n, a, b, ab, ba):
    # Declaracion de variables para la salida del algoritmo (No modificar)
    time = 0
    lines = []
    finalLine = ' '

    # Algoritmo con dinamica
    # Array para guardar el valor de la soluc¨®n optima en terminos de tiempo
    T = [[], []]
    
    # Array para guardar la matriz auxiliar de la soluci¨®n ¨®ptima, de la cual
    # luego se calcula la solucion optima
    L = [[], []]
    
    # Casos base, cuando se analiza la actividad 1
    # Recordar que por facilidad, indexamos empezando 0
    T[0,0] = a[1]
    T[1,0] = b[1]
    
    L[0,0] = 'a'
    L[1,0] = 'b'

    # Ciclo for de 1 hasta n sin incluirlo, iterando de a 1
    # Populando matriz de valor de solucion optima y matriz auxiliar
    for j in range(1,n):
        # Computar los valores de T[0,j] y L[0,j], fila 1 de cada array
        if T[0,j-1] +  a[j] <= T[1, j-1] + ba[j-1] + a[j]:
            T[0,j] = T[1, j-1] + a[j]
            L[0,j] = 'a'
        else:
            T[0,j] = T[1, j-1] + ba[j-1] + a[j]
            L[0,j] = 'b'
        
        # Computar los valores de T[1,j] y L[1,j], fila 2 de cada array
        if T[1,j-1] +  b[j] <= T[0, j-1] + ab[j-1] + b[j]:
            T[1,j] = T[1,j-1] +  b[j]
            L[1,j] = 'b'
        else:
            T[1,j] = T[0, j-1] + ab[j-1] + b[j]
            L[1,j] = 'a'
        
        
    # Calcular el valor de la solucion optima (time) y la linea de ensamblaje
    # en donde se termino el proceso, que sirve para calcular luego la 
    # solucion optima
    if(T[0,n-1] <= T[1,n]):
        time += T[0,n-1]
        finalLine='a'
    else:
        time += T[1,n-1]
        finalLine='b'
        
    
    # Fin del algoritmo

    #Salida del algoritmo (No modificar)
    return n, time, finalLine
    # Test : return n, a, b, ab, ba


## Funciones auxiliares

##Llamado a funcion por pruebas
#solve(1,2,3,4,5)