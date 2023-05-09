import numpy as np


def find_patterns(numbers):
    # Converter a lista de números em um array do NumPy
    arr = np.array(numbers)

    # Calcular as diferenças entre os elementos adjacentes
    diffs = np.diff(arr)

    # Encontrar os índices onde as diferenças são iguais
    equal_diff_indices = np.where(diffs[1:] == diffs[:-1])[0] + 1

    # Verificar se há padrões de 3 elementos consecutivos com a mesma diferença
    patterns = []
    for i in equal_diff_indices:
        if i >= 2 and diffs[i - 2] == diffs[i - 1] == diffs[i]:
            patterns.append((i - 2, i - 1, i))

    return patterns
print(find_patterns([1,2,7,4,9,5,3,6,8,0]))