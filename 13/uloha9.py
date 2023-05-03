number = int(input())
ans = ""
while ( number ):
    ans += str(number&1)
    number = number >> 1
    
ans = ans[::-1]
print(ans)