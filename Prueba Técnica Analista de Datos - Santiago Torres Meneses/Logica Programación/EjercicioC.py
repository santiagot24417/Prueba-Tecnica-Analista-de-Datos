
def main():
    p = input("\nIngresa el número correspondiente para calcular el super número: ")
    print("su super numero es: "+"\n")
    supernumero(int(p))
    while int(p) >=10:
        print("supernumero(", p, "):", supernumero(int(p)))
        p=supernumero(int(p))


def supernumero(numero):

    if numero == 0:
        return numero
    if numero < 10:
        return numero
    else:
        return numero % 10 + supernumero(numero // 10)


if __name__ == "__main__":
    main()