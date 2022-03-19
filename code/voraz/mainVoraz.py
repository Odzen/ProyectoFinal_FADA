import voraz, inOut
"""
Main para voraz
"""

#Función main
def main():
    '''
    n, a, b, ab, ba = inOut.input()
    print(n,a,b,ab,ba)
    
    resultVoraz = voraz.solve(n, a, b, ab, ba)
    inOut.output(resultVoraz)
    '''

matriz = voraz.matriz([9, 3, 4, 2, 6, 8, 2, 12, 14, 5, 2, 3, 7, 9, 2, 15, 18, 3, 7, 6, 3, 1, 2, 3],[4, 6, 2, 7, 9, 5, 2, 7, 13, 1, 5, 15, 16, 17, 3, 2, 5, 9, 9, 8, 5, 1, 2, 3],[9, 2, 8, 3, 4, 6, 2, 5, 7, 9, 6, 3, 1, 8, 3, 4, 7, 4, 2, 7, 9, 7, 5, 9, 0],[7, 4, 5, 3, 5, 7, 9, 6, 5, 3, 6, 8, 9, 6, 4, 3, 8, 9, 4, 6, 9, 4, 2, 6, 0])
cadena2 = voraz.voraz([9, 3, 4, 2, 6, 8, 2, 12, 14, 5, 2, 3, 7, 9, 2, 15, 18, 3, 7, 6, 3, 1, 2, 3],[4, 6, 2, 7, 9, 5, 2, 7, 13, 1, 5, 15, 16, 17, 3, 2, 5, 9, 9, 8, 5, 1, 2, 3], matriz)
print(cadena2)
'''
matriz = voraz.matriz([7,9,3,4,8,4],[8,5,6,4,5,7],[2,1,2,2,1],[2,3,1,3,4])
cadena2 = voraz.voraz([7,9,3,4,8,4],[8,5,6,4,5,7],matriz)
print (cadena2)
cadena = "funcionaaaa"
print(cadena)
'''
if __name__ == "__main__":
    main()