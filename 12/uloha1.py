

x = int(input())
y = int(input())

dni = 1

while x < y:
    dni += 1
    x = x + x*0.1

print(dni)
print(round(x))
