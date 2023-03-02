def reverter(cadeia):
    revertido = ""

    for caractere in cadeia:
        revertido = caractere + revertido

    return revertido


def reverter2(cadeia):
    # Truque interessante de Python para reverter listas e strings
    return cadeia[::-1]


def main():
    print(reverter("Guilherme"))


if __name__ == "__main__":
    main()