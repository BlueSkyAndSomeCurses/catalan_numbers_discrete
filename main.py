"""
Catalan
"""
def diagonal_counting(n_elem):
    '''
    Return a number of diagonals in Polygon
    '''
    n_elem_div = n_elem // 2
    if n_elem == 0:
        return 1
    catalan = [0] * (n_elem_div + 1)
    catalan[0] = 1
    for i in range(1, n_elem_div + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - 1 - j]
    return catalan[n_elem_div]


print(diagonal_counting(6))

if __name__ == "__main__":
    diagonal_counting(4)
