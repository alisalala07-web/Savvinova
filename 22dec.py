#1
"""
n = int(input())
def factorial(n):
    if n >= 1:
        return n * factorial(n-1)
    return 1
print(factorial(n))
"""
#2
"""
string = input()
vowels = ['a', 'e','y', 'u', 'i', 'o']
def remove_vowels(string):
    if string == "":
        return ""
    s = string[0]
    if s in vowels:
        return remove_vowels(string[1:])
    return s + remove_vowels(string[1:])
print(remove_vowels(string))
"""
#3
"""
n = int(input())
def paskal(n):
    if n == 1:
        return [1]
    p = paskal(n-1)
    p1 = [1]
    for i in range(len(p)-1):
        p1.append(p[i] + p[i + 1])
    p1.append(1)
    return p1
print(paskal(n))
"""