import voraz, inOut
"""
Main para voraz
"""

#Función main
def main():
    n, a, b, ab, ba = inOut.input()
    resultVoraz = voraz.solve(n, a, b, ab, ba)
    inOut.output(resultVoraz)


if __name__ == "__main__":
    main()