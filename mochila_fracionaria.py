"""Algoritmo da mochila fracionária, onde a partir de uma tabela de itens,
é acrescentado a mochila os produtos com maior preço por peso buscando 
assim, obter o maior valor possível de roubo, sempre respeitando a capacidade
de armazenamento da mochila
"""


import pandas as pd
import os


def mostrar_itens():
    """Imprime tabela de informações dos itens."""
    print("-"*28)
    print("{:>14}" .format('ITENS'))
    print("-"*28)
    estoque = pd.DataFrame(data=itens)
    print(estoque)
    print("-"*28)


def mochila_fracionaria(itens, peso_mochila):
    """A função executa o algoritmo da mochila fracionária.

    A função busca o item de maior valor por peso e acrescenta a mochila,
    se necessário os itens podem ser fracionados até que a mochila comporte
    seu peso total permitido.

    param: dict com informações dos itens e o peso que a mochila comporta.
    return: list com quantidade roubada de cada item.
    """
    peso_atual = 0
    # List com quantidade de cada item roubado
    roubado = [0 for i in itens['item']]
    beneficio = list(map(lambda valor, peso: valor/peso,
                         itens["valor"], itens["peso"]))

    # Busca o produto de maior valor por peso e o acrescenta a mochila
    # Caso o item não possa ser subtraído por inteiro, este é acresentado de forma fracionada
    while peso_atual < peso_mochila:
        i = beneficio.index(max(beneficio))
        beneficio[i] = 0
        roubado[i] = min(itens["peso"][i], peso_mochila - peso_atual)
        peso_atual += roubado[i]

    return roubado


def mostra_roubo(itens, roubado):
    """Imprime os itens e que foram roubados e respectivas informações.

    param: dict com informações dos itens e list da quantidade de itens roubados.
    """
    valor_ganho = 0

    os.system("cls")
    print("-"*22)
    print("{:>18}" .format('ITENS ROUBADOS'))
    print("-"*22)
    for i in range(len(roubado)):
        if roubado[i] != 0:
            print(f'Item roubado: {itens["item"][i]}')
            print(f'Quantidade: {roubado[i]}(kg/ml)')
            print(
                f'Valor subtraído: {(itens["valor"][i]/itens["peso"][i])*roubado[i]:.02f}')
            valor_ganho += (itens["valor"][i]/itens["peso"][i])*roubado[i]
            print("-"*22)
    print(f"Total subtraído: {valor_ganho:.02f}")
    print("-"*22)


itens = {
    "item": ['arroz', 'feijão', 'carne', 'óleo', 'café', 
            'macarrão', 'refrigerante', 'leite', 'sal', 'açucar'],
    "valor": [25.00, 6.00, 30.00, 7.00, 8.00, 3.00, 5.00, 3.00, 2.00, 2.00],
    "peso": [5, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}

while True:
    mostrar_itens()
    peso_mochila = int(input("Qual o peso que a mochila suporta?(kg): "))
    roubado = mochila_fracionaria(itens, peso_mochila)
    mostra_roubo(itens, roubado)

    novo = str(input("Fazer de novo?(s/n): "))
    if novo == 's':
        os.system("cls")
        continue
    else:
        break
