a=int(input())
for b in range(a):
    x,y=map(int,input().split())
    if(x>=y):
        print("YES")
    else:
        print("NO")
