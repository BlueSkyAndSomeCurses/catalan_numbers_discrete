"""
Catalan
"""
def factorial_recursive(number):
    '''
    Recursive function, returns a factorial of number
    '''
    factorial = 1
    if number != 1:
        factorial *= (number * (factorial_recursive(number - 1)))
    else:
        return 1
    return factorial


def ways_to_dot(n_elem):
    '''
    Returns number of ways from (0,0) to (n,n)
    '''
    result = (factorial_recursive(2* n_elem) // \
(factorial_recursive(n_elem) * factorial_recursive(2* n_elem - n_elem))) // (n_elem + 1)
    return result

if __name__ == "__main__":
    pass
