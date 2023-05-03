
n = int(input("Zadaj n: "))
try:
    print(f"1 / {n} = {1/n}")
except ZeroDivisionError:
    print("Nulou deliť neviem")
