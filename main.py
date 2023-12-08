"""
Catalan
"""

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

for i in n: 
    print(i)

if __name__ == "__main__":
    pass
