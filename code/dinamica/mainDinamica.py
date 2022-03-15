import dinamica
#from ..inOut import *
import inOut

"""
Main para dinamica
"""

#Funcion main
def main():
    n, a, b, ab, ba = inOut.input()
    resultDinamic = dinamica.solve(n, a, b, ab, ba)
    inOut.output(resultDinamic)
    
    #Resturn test, antes de escribir en archivo
    # For test
    # print(resultDinamic)

if __name__ == "__main__":
    main()