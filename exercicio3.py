import json

def ler_json(arquivo):
    # Lê o arquivo JSON e retorna uma lista com os valores dos dias.
    with open(arquivo) as arquivo_json:
        objeto_json = json.load(arquivo_json)
        return [dia["valor"] for dia in objeto_json]


def media(lista_numeros):
    soma = 0
    tamanho = 0

    for numero in lista_numeros:
        if numero == 0.0:
            continue

        soma += numero
        tamanho += 1

    return soma / tamanho 
        

def main():
    arquivo_json = "dados.json"
    valores_diarios = ler_json(arquivo_json)
    
    # Parte-se do pressuposto de que a primeira posição contém o menor e o maior valor,
    # que posteriormente são comparados ao resto dos valores da lista
    valor_min = valores_diarios[0]
    valor_max = valores_diarios[0]

    dias_superiores_media = 0
    media_diaria = media(valores_diarios)

    for valor in valores_diarios:
        # Pulando os dias sem faturamento
        if valor == 0.0:
            continue

        if valor_min > valor:
            valor_min = valor
        
        if valor_max < valor:
            valor_max = valor

        if valor > media_diaria:
            dias_superiores_media += 1

    print(f"Menor valor: {valor_min}")
    print(f"Maior valor: {valor_max}")
    print(f"Quantidade de dias com faturamento superior à média: {dias_superiores_media}")


if __name__ == "__main__":
    main()