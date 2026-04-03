def bubble_sort_bidirectional(arr):
    """
    Implementação do Bubble Sort Bidirecional
    Leva o maior para a direita e o menor para a esquerda na mesma iteração.
    """
    n = len(arr)
    left = 0
    right = n - 1
    
    while left < right:
        # Direita: leva o maior para o final
        for i in range(left, right):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1
        
        # Esquerda: traz o menor para o início
        for i in range(right, left, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        left += 1
    return arr

def linear_search(arr, target):
    """Retorna o número de passos e o índice"""
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            return i, steps
    return -1, steps

def binary_search(arr, target):
    """Busca binária"""
    steps = 0
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        steps += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1, steps