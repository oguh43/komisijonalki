
pocet = int(input("Zadaj pocet: "))

if pocet == 0:
    print("Hráš férovo")
elif 1 <= pocet <= 2:
    print("Máš žltú kartu")
elif 3 <= pocet <= 5:
    print("Máš fialovú kartu")
elif pocet > 5:
    print("Máš červenú kartu")

