def pertence_fibonacci(numero):
    # Variáveis com os valores iniciais da sequência
    a = 0
    b = 1

    while a <= numero:
        if numero == a:
            return True

        a, b = b, a + b

    return False


def main():
    numero = int(input("Digite um número inteiro: "))

    if pertence_fibonacci(numero):
        print(f"O número {numero} pertence à sequência de Fibonacci")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci")


if __name__ == "__main__":
    main()