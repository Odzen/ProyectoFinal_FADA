import pylab as plt
import dinamica
import inOut
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
Funcion plotting_incremental

Recibe un numero de actividades que pasaran por las dos lineas de ensamblaje, e itera desde 1 hasta
numero de actividades, con la ayuda del test_creation:
Ejemplo si el numero de actividades es igual a 10, creara 10 pruebas
la primera con 1 actividad, la segunda con 2 actividades etc..

Para estas pruebas se puede calcular tanto tiempo del algoritmo de dinamica como el de voraz
Solo se necesitaria cambiar una sola linea

Por ultimo se calcula el tiempo medio y se grafica. lineasEnsamblaje vs Tiempo
"""

def plotting_incremental(numeroActividades):
    
    actividades = []
    times = []
    meanTime = 0
    
    for actividad in range(1, numeroActividades):
        
        n, a, b, ab, ba = test_creation.test_creation(actividad,actividad)
        #n, a, b, ab, ba = inOut.input()
        
        # En este caso se prueba con dinamica, se podria probar con voraz
        start = time.time()
        dinamica.solve(n, a, b, ab, ba)
        end = time.time()
        timeTotalMachine = end - start
        
        actividades.append(actividad)
        times.append(timeTotalMachine)
                
        #print(decimal.Decimal(timeTotalMachine))
    
    #Calcular tiempo medio:
    meanTime = sum(times) / len(times)
    print(meanTime)
    
    # Plot    
    plt.figure('plot1')
    plt.title('Actividades incrementales')
    plt.xlabel('Actividades')
    plt.ylabel('tiempo (s)')
    plt.plot(actividades,times)
    
    return meanTime
    
    
        
# Prueba 1 , secuencial - dinamica - y numero de pruebas = 1000    
plotting_incremental(1000)
    

"""
Funcion plotting_redundante

Recibe un numeroPrueba y un n_veces, el cual es el numero de prueba que se va a ejecutar, de las pruebas
ya existentes en el directorio de pruebas, archivos in.txt

La idea es que se ejecute esa prueba n_veces, poder graficar el comportamiento y sacar tiempo medio

Para estas pruebas se puede calcular tanto tiempo del algoritmo de dinamica como el de voraz
Solo se necesitaria cambiar una sola linea

Por ultimo se calcula el tiempo medio y se grafica. numeroPrueba vs Tiempo
"""

def plotting_redundante(numeroPrueba, n_veces):
    n, a, b, ab, ba = inOut.input(numeroPrueba)
    pruebas = []
    times = []
    meanTime = 0
    
    for prueba in range(1,n_veces):
        # En este caso se prueba con dinamica, se podria probar con voraz
        start = time.time()
        dinamica.solve(n, a, b, ab, ba)
        end = time.time()
        timeTotalMachine = end - start
        
        pruebas.append(prueba)
        times.append(timeTotalMachine)
        
    #Calcular tiempo medio:
    meanTime = sum(times) / len(times)
    print("Tiempo medio para la prueba del archivo in"+numeroPrueba+".txt es: "+ str(meanTime))
    
    # Plot    
    plt.figure('plot2')
    plt.title('Actividad constante - N veces')
    plt.xlabel('numero de prueba')
    plt.ylabel('tiempo (s)')
    plt.plot(pruebas,times)
    
    return meanTime

plotting_redundante("8", 500)



    
# voraz vs dinamica, overlaying plots y agregar labels y cambiando el display
# se puede usar subplots tambien 



 # Way 2 - time
 #timeMachineList = timeit.repeat(lambda: dinamica.solve(n, a, b, ab, ba), number=1, repeat=1)
 #print(timeMachineList)
 #timeMachine= Decimal(sum(timeMachineList)) / len(timeMachineList)
 #0.00011 con Test 3
    
 #print(timeMachine)