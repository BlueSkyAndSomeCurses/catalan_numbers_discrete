"""
Catalan
"""
# def factorial_recursive(number):
#     '''
#     Recursive function, returns a factorial of number
#     '''
#     factorial = 1
#     if number != 1:
#         factorial *= (number * (factorial_recursive(number - 1)))
#     else:
#         return 1
#     return factorial


# def ways_to_dot(n_elem):
#     '''
#     Returns number of ways from (0,0) to (n,n)
#     '''
#     result = (factorial_recursive(2* n_elem) // \
# (factorial_recursive(n_elem) * factorial_recursive(2* n_elem - n_elem))) // (n_elem + 1)
#     return result

def ways_to_dot(n_elem):
    '''
    Returns how many ways you can find in nxn matrix
    '''
    matrix = [[0] * (n_elem + 1) for _ in range(n_elem + 1)]

    for i in range(n_elem + 1):
        matrix[i][0] = 1
    for j in range(n_elem + 1):
        matrix[0][j] = 1
    for i in range(1, n_elem + 1):
        for j in range(1, n_elem + 1):
            matrix[i][j] =matrix[i - 1][j] + matrix[i][j - 1]
    return (matrix[n_elem][n_elem]) // (n_elem + 1)


if __name__ == "__main__":
    ways_to_dot(10)
