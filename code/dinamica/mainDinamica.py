import dinamica
import inOut

"""
Main para dinamica

Para cambiar el # de la prueba, solo cambie la variable global 'numeroPrueba', 
dependiendo de que prueba se quiera escoger del directorio Pruebas/Tests_in_files
"""

numeroPrueba = "12"

#Funcion main
def main():
    n, a, b, ab, ba = inOut.input(numeroPrueba)
    
    #n=12
    #a= [88, 97, 72, 31, 25, 6, 21, 58, 42, 5, 23, 9]
    #b= [46, 4, 90, 57, 81, 19, 12, 97, 22, 54, 35, 97]
    #ab=[2, 4, 48, 20, 24, 7, 18, 25, 14, 10, 8]
    #ba=[36, 26, 11, 41, 10, 23, 30, 41, 9, 45, 3]
    
    resultDinamic = dinamica.solve(n, a, b, ab, ba)
    inOut.output(resultDinamic, numeroPrueba)
        
    
    
    #Resturn test, antes de escribir en archivo
    # For test
    print(resultDinamic)

if __name__ == "__main__":
    main()