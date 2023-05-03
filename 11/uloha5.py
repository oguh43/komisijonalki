from random import randint

s = 0
ine = 0
r = 0

for _ in range(10):
    r = randint(1, 6)
    if r == 6:
        s += 1
    else:
        ine += 1
    print(r)
print(f"Padlo {s} šestiek a {ine} iných čísel")






