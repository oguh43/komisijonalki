n = int(input())
ls = [0,1]
print(0)
print(1)
while sum(ls[-2:]) < n:
    ls.append(sum(ls[-2:]))
    print(ls[-1])


