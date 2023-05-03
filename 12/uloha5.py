
num = int(input())
cs = 0

while num!=0:
    cs = cs + num % 10
    print(num % 10)
    num = num // 10


print(cs)




