"""
Catalan
"""
import functools
import time

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


@functools.lru_cache(maxsize=1000)
def catalan_recursive(n: int):
    match n:
        case 0:
            return 1
        case 1:
            return 1
        case 2:
            return 2
        case 3:
            return 5

    catalan = 0
    for k in range(n):
        catalan += catalan_recursive(k) * catalan_recursive(n - k - 1)

    return catalan


def recursive_definition(n):
    for i in range(n + 1):
        print(i, ":", catalan_recursive(i))


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

def catalan_powers(x, numb):
    def factorial(m):
        '''
        factorial
        '''
        if m == 0:
            return 1
        return m * factorial(m - 1)

    def ceshka(n, k):
        '''
        Counts number of nth number by ceshka
        '''
        return factorial(n) // (factorial(k) * factorial(n - k))

    def counted_catalan_number(n):
        '''
        Counts by fromula of counting C(n) = (1/(n+1)) * C(2 * n, n)
        '''
        return ceshka(2 * n, n) // (n + 1)

    def catalan_power_series_method(x, numb_of_first_terms):
        '''
        Finds sum of n terms.
        '''
        series = [counted_catalan_number(n) * (x ** n) for n in range(numb_of_first_terms)]
        return sum(series)

    return catalan_power_series_method(x, numb)

def parentheses(n: int) -> list[str]:
    res = []
    def dfs(left, right, s):
        if len(s) == n * 2:
            res.append(s)
            return
        if left < n:
            dfs(left + 1, right, s + '(')
        if right < left:
            dfs(left, right + 1, s + ')')
    dfs(0, 0, '')
    return res

p=parentheses(10)
for i in p:
    print(i)

if __name__ == "__main__":
    diagonal_counting(4)
    ways_to_dot(10)
    print(diagonal_counting(20))
    print(ways_to_dot(10))
    
    start = time.time()
    recursive_definition(1000)
    print(time.time())

