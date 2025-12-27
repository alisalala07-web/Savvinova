#олимпиадное программирование

#1

def lis(arr):
    d = [1]*len(arr)
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                d[i] = max(d[i], d[j]+1)
    return max(d)

print(lis([6,2,5,4,2,5,6]))

#2

