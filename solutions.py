import math

# Exercício 1: List Comprehension
def filter_whitespace(text):
    return [char for char in text if not char.isspace()]

# Exercício 5: O(N²) para O(N)
def find_max_optimized(arr):
    # O(N²) original geralmente usa loops aninhados.
    # O(N) usa apenas uma passagem.
    if not arr: return None
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

# Exercício 6: Grãos de Arroz no Xadrez
def find_chess_square(grains):
    """
    1 grão -> q1 (2^0)
    2 grãos -> q2 (2^1)
    4 grãos -> q3 (2^2)
    A fórmula é: grãos = 2^(quadrado - 1)
    Logo: log2(grãos) = quadrado - 1  => quadrado = log2(grãos) + 1
    """
    if grains <= 0: return 0
    return int(math.log2(grains)) + 1

# Explicação Big O do Exercício 6: 
# A complexidade é O(1) se considerarmos a função logarítmica constante,
# ou O(log N) se implementada via loop de divisões por 2.