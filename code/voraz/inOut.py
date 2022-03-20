nombreLectura = "in"
nombreEscritura = "out"

'''
input()
Funcion para leer el archivo bajo el formato establecido en el proyecto. El
nombre se cambia en la variable global "nombreLectura". (No modificar)
'''

def input(numeroPrueba):
    with open("../../Pruebas/Tests_in_files/"+nombreLectura+numeroPrueba+".txt", "r") as f:
        content = f.read().split('\n')
        n = int(content[0])
        a = list(map(lambda x: int(x), content[1].split(" ")))
        b = list(map(lambda x: int(x), content[2].split(" ")))
        ab = list(map(lambda x: int(x), content[3].split(" ")))
        ba = list(map(lambda x: int(x), content[4].split(" ")))
        return n, a, b, ab, ba

'''
output()
Funcion para escribir sobre el archivo segun lo solicitado en el proyecto. El
nombre del archivo se cambia en la variable global "nombreEscritura". (No modificar método)
'''

'''
Las salidas de los archivos se guardaran la carpeta Pruebas/outDinamica/
Para la prueba ini.txt el archivo de salida sera outi.txt, siendo i el 
'numeroPrueba', variable global definida anteriormente
'''

def output(output, numeroPrueba):
    n, time, lines = output
    toWrite = ""
    toWrite += str(n) + "\n"
    toWrite += str(time)
    for line in lines:
        toWrite += "\n" + str(line)

    with open("../../Pruebas/outVoraz/"+nombreEscritura+numeroPrueba+".txt", "w") as f:
        f.write(toWrite)



