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
    
    resultDinamic = dinamica.solve(n, a, b, ab, ba)
    inOut.output(resultDinamic, numeroPrueba)
    
    #Resturn test, antes de escribir en archivo
    # For test
    print(resultDinamic)

if __name__ == "__main__":
    main()