def freq(n):
    uni = {}
    for i in n:
        if i in uni:
            uni[i] += 1
        else:
            uni[i] = 1
    return uni

nums = list(map(int, input().split()))
resultado = freq(nums)
for i in resultado:
    print(f"{i}: {resultado[i]}")