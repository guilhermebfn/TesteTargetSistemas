import json

def lerJson(arquivo):
    # Lê o arquivo JSON e retorna uma lista com os valores dos dias.
    with open(arquivo) as arquivoJson:
        objetoJson = json.load(arquivoJson)
        return [dia["valor"] for dia in objetoJson]


def media(listaNumeros):
    soma = 0
    tamanho = 0

    for numero in listaNumeros:
        if numero == 0.0:
            continue

        soma += numero
        tamanho += 1

    return soma / tamanho 
        

def main():
    arquivoJson = "dados.json"
    valoresDiarios = lerJson(arquivoJson)
    
    # Parte-se do pressuposto de que a primeira posição contém o menor e o maior valor,
    # que posteriormente são comparados ao resto dos valores da lista
    valorMin = valoresDiarios[0]
    valorMax = valoresDiarios[0]

    diasSuperioresMedia = 0
    mediaDiaria = media(valoresDiarios)

    for valor in valoresDiarios:
        # Pulando os dias sem faturamento
        if valor == 0.0:
            continue

        if valorMin > valor:
            valorMin = valor
        
        if valorMax < valor:
            valorMax = valor

        if valor > mediaDiaria:
            diasSuperioresMedia += 1

    print(f"Menor valor: {valorMin}")
    print(f"Maior valor: {valorMax}")
    print(f"Quantidade de dias com faturamento superior à média: {diasSuperioresMedia}")


if __name__ == "__main__":
    main()