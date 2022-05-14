def main():
    while True:
        reducir.divisor = 2  # Variable estática
        numerador, denominador = input("\nIngresa los valores separados por un espacio: ").split()
        if (int(numerador) <= 0 or int(denominador) <= 0):
            main()
        else:
            reducir(int(numerador), int(denominador))




def reducir(numerador, denominador):

    num = float(numerador) / reducir.divisor
    den = float(denominador) / reducir.divisor


    if (num.is_integer() and den.is_integer()):
        print(num, "/", den)
        reducir(num, den)
    else:

        if (reducir.divisor == numerador or reducir.divisor == denominador or num <= 1 or den <= 1):
            print("La mínima expresión es: ", numerador, "/", denominador)
        else:

            reducir.divisor += 1
            reducir(numerador, denominador)


if __name__ == "__main__":
    main()