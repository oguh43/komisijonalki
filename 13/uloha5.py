ls = []
inp = -1
while inp != 0:
    inp = int(input())
    if inp != 0:
        ls.append(inp)

print(len(ls))
print(sum(ls))
s = 1
for i in ls:
    s *= i
print(s)
print(sum(ls)/len(ls))
print(min(ls))
print(max(ls))
