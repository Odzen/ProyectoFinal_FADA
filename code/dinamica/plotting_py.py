import pylab as plt
import dinamica
#import inOut
import test_creation
#way 1
import time

#way 2
#import timeit
#import decimal
"""
Representar graficamente los algoritmos en tiempo, para poder determinar
su eficiencia y compararlo con la complejidad teorica
"""

"""
Recibe un numero de pruebas, y crea un numero de pruebas desde 1 hasta
numero de pruebas, con la ayuda del test_creation:
Ejemplo si el numero de pruebas es igual a 10, creara 10 pruebas
la primera con 1 linea de ensamblaje, la segunda con 2 lineas de ensamblajes etc..

Para estas pruebas se puede calcular tanto tiempo del algoritmo de dinamica como el de voraz
Solo se necesitaria cambiar una sola linea
"""

def plotting_secuencial(numeroPruebas):
    
    pruebas = []
    times = []
    meanTime = 0
    
    for prueba in range(1, numeroPruebas):
        
        n, a, b, ab, ba = test_creation.test_creation(prueba,prueba)
        #n, a, b, ab, ba = inOut.input()
        
        # En este caso se prueba con dinamica, se podria probar con voraz
        start = time.time()
        dinamica.solve(n, a, b, ab, ba)
        end = time.time()
        timeTotalMachine = end - start
        
        pruebas.append(prueba)
        times.append(timeTotalMachine)
                
        #print(decimal.Decimal(timeTotalMachine))
    
    #Calcular tiempo medio:
    meanTime = sum(times) / len(times)
    print(meanTime)
    
    # Plot    
    plt.figure('plot1')
    plt.title('Pruebas secuenciales')
    plt.xlabel('numero de prueba')
    plt.ylabel('tiempo (s)')
    plt.plot(pruebas,times)
    
    return meanTime
    
    
        
# Prueba 1 , secuencial - dinamica - y numero de pruebas = 1000    
plotting_secuencial(1000)
    



    
# voraz vs dinamica, overlaying plots y agregar labels y cambiando el display
# se puede usar subplots tambien 



 # Way 2 - time
 #timeMachineList = timeit.repeat(lambda: dinamica.solve(n, a, b, ab, ba), number=1, repeat=1)
 #print(timeMachineList)
 #timeMachine= Decimal(sum(timeMachineList)) / len(timeMachineList)
 #0.00011 con Test 3
    
 #print(timeMachine)