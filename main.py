from algorithms import bubble_sort_bidirectional, linear_search, binary_search
from solutions import filter_whitespace, find_max_optimized, find_chess_square

def run_tp():
    print("--- Exercício 1: List Comprehension ---")
    string_b3 = "Sítio do pica-pau amarelo \n 2023"
    print(filter_whitespace(string_b3))

    print("\n--- Exercício 2: Algoritmo das Cartas ---")
    print("Passos sugeridos: ")
    print("1. Pegar a carta visível com a mão livre.")
    print("2. Comparar com as cartas já ordenadas na outra mão.")
    print("3. Inserir na posição correta (frente/trás/entre dedos).")
    print("Isso descreve logicamente um Insertion Sort (Ordenação por Inserção).")

    print("\n--- Exercício 3 e 4: Passos de Busca ---")
    arr_sorted = [2, 4, 6, 8, 10, 12, 13]
    _, steps_linear = linear_search(arr_sorted, 8)
    _, steps_binary = binary_search(arr_sorted, 8)
    print(f"Busca Linear por '8': {steps_linear} passos.")
    print(f"Busca Binária por '8': {steps_binary} passos.")

    print("\n--- Exercício 8: Bubble Sort Bidirecional ---")
    nums = [64, 34, 25, 12, 22, 11, 90]
    strs = ["Vasco", "Itaú", "Angular", "Python", "NTT"]
    print(f"Números ordenados: {bubble_sort_bidirectional(nums)}")
    print(f"Strings ordenadas: {bubble_sort_bidirectional(strs)}")

    print("\n--- Exercício 6: Xadrez ---")
    graos = 16
    print(f"Para {graos} grãos, o quadrado é: {find_chess_square(graos)}")

if __name__ == "__main__":
    run_tp()