x=int(input())
n = int(input())

ans = 1

while n > 0:
    
    ans *= x
    
    n -= 1
    
print(ans)
