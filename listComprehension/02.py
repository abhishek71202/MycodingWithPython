'''
anylist=[1,2,3,4,5]
newlist=[x for x in anylist ]#if x>3]


for i in anylist:
    #newlist.append(i)
    
    if i<3:
        newlist.append(i)
   
print(newlist)
print(len(newlist))

'''
x=int(input())
z=int(input())
b=int(input())
y=[p for p in range(x+1)]
a=[q for q in range(z+1)]
perm=[[i,j]for i in y for j in a]
#req= [l for l in perm if sum (l)!=b]
print(y)
