def scholership(k):
    if k >= 1 and k <= 50:
         return 100
    elif k >= 51 and k <= 100:
        return 50
    else:
        return 0
k = int(input())
print(scholership(k))