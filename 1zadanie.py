#1 
"""
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if 1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
    A = x1 - x2
    B = y1 - y2 
    if A * A + B * B == 5:
        print("yes")
    else:
        print("no")
else:
    print("Ошибка!")
"""
#2
"""
K = int(input())
N = int(input())
sum = 0
for i in range(K, N + 1):
    if i % 2 == 0:
        sum += i
        print(sum)
"""
#3
"""
x = 0
while True:
    y = int(input())
    if y == 0:
        break
    x += y
print(x)
"""
#4
"""
N = int(input())
factorial = 1
for i in range(1, N + 1):
    factorial *= i
print(factorial)
"""
