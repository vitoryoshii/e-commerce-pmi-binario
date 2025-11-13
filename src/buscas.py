"""
===========================================================
COMPARATIVO DE ALGORITMOS DE BUSCA - LINEAR X BINÁRIA

Descrição:
    Módulo que implementa dois algoritmos clássicos de busca:
    - Busca Linear (ou Sequencial)
    - Busca Binária

    Com o objetivo de comparar o desempenho e a eficiência de ambas,
    demonstrando a diferença entre percorrer todos os elementos
    (busca linear) e reduzir o problema pela metade a cada iteração
    (busca binária).

    A busca binária exige que os dados estejam **ordenados**,
    enquanto a busca linear pode ser aplicada em qualquer lista.

===========================================================
"""


# ===========================================================
# FUNÇÕES DE BUSCA BINÁRIA E LINEAR
# ===========================================================


def busca_linear(lista, alvo):
    """
    Realiza uma busca linear (sequencial) em uma lista.
    
    Parâmetros:
        lista (list): lista de elementos a serem percorridos
        alvo (int): valor a ser encontrado

    Retorna:
        tuple(bool, int): 
            - True se o elemento for encontrado, False caso contrário
            - Quantidade de passos realizados até o término da busca
    """

    passos = 0
    for item in lista:
        passos += 1
        if item == alvo:
            return True, passos
    return False, passos


def busca_binaria(lista, alvo):
    """
    Realiza uma busca binária em uma lista ORDENADA.
    
    Parâmetros:
        lista (list): lista ordenada de elementos
        alvo (int): valor a ser encontrado

    Retorna:
        tuple(bool, int): 
            - True se o elemento for encontrado, False caso contrário
            - Quantidade de passos realizados até o término da busca

    Observação:
        A busca binária divide o problema pela metade a cada iteração,
        tornando uma busca muito mais eficiente que a busca linear.
    """
    
    esquerda = 0
    direita = len(lista) - 1
    passos = 0
    while esquerda <= direita:
        passos += 1
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return True, passos
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return False, passos
