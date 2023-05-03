n = list(input())
tmp = n[0]
n[0] = n[-1]
n[-1] = tmp
print("".join(n))