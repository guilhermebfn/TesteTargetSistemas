def ler_valor(estados):
    faturamento_por_estado = dict()

    for estado in estados.split('\n'):
        nome_estado = estado.lstrip().split(" ")[0]
        valor_string = estado.lstrip().split(" ")[2] # Representação intermediária (p.ex. R$45.000,00)
        valor_estado = float(valor_string.lstrip('R$')
                                   .replace(".", "")
                                   .replace(",", "."))
        faturamento_por_estado[nome_estado] = valor_estado
    
    return faturamento_por_estado


def main():
    estados = """SP – R$67.836,43
                 RJ – R$36.678,66
                 MG – R$29.229,88
                 ES – R$27.165,48
                 Outros – R$19.849,53"""

    faturamento_por_estado = ler_valor(estados)
    faturamento_total = sum(faturamento_por_estado.values())

    for estado, faturamento in faturamento_por_estado.items():
        print(f"O percentual total de faturamento de {estado} sobre o total foi {100 * faturamento / faturamento_total:.2f}%")


if __name__ == "__main__":
    main()