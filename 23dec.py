#1
"""
def n(a, b):
    if a > b:
        return 0
    if a == b:
        return 1
    return n(a + 1, b)+n(a+2, b)+n(a*2, b)
print(n(3, 10) * n(10, 12))
"""
#2
"""
def f(a, b):
    if a == 26 or a > b:
        return 0
    if a == b:
        return 1
    return f(a + 1, b)+f(2 * a + 1, b)
print(f(1, 27))
"""
#3
"""
def s(a, b, n):
    if a > b or a == n:
        return 0
    if a == b:
        return 1
    return s(a + 1, b, n)+s(a + 2, b, n)
print(s(2, 9, 14) * s(9, 18, 14))
"""