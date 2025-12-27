#Обработка символьных строк 23.12
#1
"""
with open("27686.txt", "r") as f:
    s = f.read()
    mx = 0
    cur = 0
    for c in s:
        if c == 'X':
            cur += 1
            if cur > mx:
                mx = cur
        else:
            cur = 0
    print(mx)
"""
#2
"""
with open("36037.txt", "r") as f:
    s = f.read()
    mx = 0
    cur = 0
    i = 0
    while i < len(s):
        if i <= len(s) - 4 and s[i:i + 4] == "XZZY":
            if cur > mx:
                mx = cur
            cur = 0
            i += 4
        else:
            cur += 1
            i += 1
    if cur > mx:
        mx = cur

    print(mx)
"""
#3
"""
with open("46982.txt", "r") as f:
    s = f.read()
    cnt = 0
    i = 0
    while i < len(s):
        if s[i] == 'E':
            j = i + 1
            bad = False
            while j < len(s) and s[j] != 'E':
                if s[j] == 'F':
                    bad = True
                    break
                j += 1
            if j < len(s) and s[j] == 'E' and not bad:
                ln = j - i + 1
                if ln >= 12 and 'E' not in s[i + 1:j]:
                    cnt += 1
                    i = j
                else:
                    i += 1
            else:
                i += 1
        else:
            i += 1
    print(cnt)
"""