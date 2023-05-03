from random import randint

teraz = 0
predtym = -1

premie = 0

for _ in range(10):
    predtym = teraz
    teraz = randint(1, 6)
    if predtym == teraz:
        premie += 1
    print(teraz)


print(f"Prémie {premie}")














