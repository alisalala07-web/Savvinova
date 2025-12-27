#двумерные массивы 18.12

# 1
"""
with open("39762.txt", "r") as f:
    n = f.readlines()
    n = [int(e1) for e1 in n]
    c = 0
    m = 0
    for i in range(len(n) - 1):
        if ((n[i] * n[i + 1]) % 15) == 0 and ((n[i] + n[i + 1]) % 7) == 0:
            c+= 1
            if m < (n[i] + n[i + 1]):
                m = (n[i] + n[i + 1])
    print(c)
    print(m)
"""
# 2
"""
with open("68279.txt", "r") as f:
    n = [int(el) for el in f]
    m = 0

    for el in n:
        if str(el)[-3:] == "562":
            if m < el:
                m= el
    c = 0
    ms = 0
    for i in range(len(n) - 3):
        l = [n[1], n[i + 1], n[i + 2], n[i + 3]]
        l5 = [el for el in l if len(str(el)) == 5]
        lnot5 = [el for el in l if len(str(el)) != 5]
        lcrat3 = [el for el in l if el % 3 == 0]
        lcrat7 = [el for el in l if el % 7 == 0]
        if len(l5) >= 1 and len(lnot5) >= 2:
            if len(lcrat3) < len(lcrat7):
                if sum(l) > m and sum(l) < m * 2:
                    c += 1
                    if ms< sum(l):
                        ms = sum(l)
    print(c)
    print(ms)
"""
# 3
"""
with open("40992.txt", "r") as f:
    n = f.readlines()
    n = [int(e1) for e1 in n]

    c = 0
    s= 0

    for el in n:
        if (el % 2) != 0:
            s += el
            c += 1

    s1 = s / c

    c = 0
    ms = 0

    for i in range(len(n) - 1):
        if (n[i] % 5) == 0 or (n[i + 1] % 5) == 0:
            if n[i] < s1 or n[i + 1] < s1:
                c += 1
                if ms < (n[i] + n[i + 1]):
                    ms = n[i] + n[i + 1]

    print(c)
    print(ms)
"""