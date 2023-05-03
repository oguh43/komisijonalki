
pocet = int(input("Zadaj pocet: "))

if pocet <= 5:
    print(f"Za {pocet} kopčekov zaplatíš {pocet * 1.1} eurá")
else:
    print(f"Za {pocet} kopčekov zaplatíš {pocet * 0.9} eurá")

