import dinamica, inOut
"""
Main para dinamica
"""

#Función main
def main():
    n, a, b, ab, ba = inOut.input()
    resultDinamic = dinamica.solve(n, a, b, ab, ba)
    inOut.output(resultDinamic)


if __name__ == "__main__":
    main()