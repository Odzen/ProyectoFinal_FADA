import voraz
import inOut
"""
Main para voraz

Para cambiar el # de la prueba, solo cambie la variable global 'numeroPrueba', 
dependiendo de que prueba se quiera escoger del directorio Pruebas/Tests_in_files
"""


numeroPrueba = "12"
#Función main
def main():
    
    n, a, b, ab, ba = inOut.input(numeroPrueba)
    
    resultVoraz = voraz.solve(n, a, b, ab, ba)
    inOut.output(resultVoraz,numeroPrueba)
    
    print(resultVoraz)
    

if __name__ == "__main__":
    main()