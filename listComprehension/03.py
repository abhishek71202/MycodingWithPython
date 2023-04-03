list1=[1,2]#(x,y) (1,3) (1,4) (2,3) (2,4)
list2=[3,4]
list3=[5,6]
newlist = [(x,y,z) for x in list1 for y in list2 for z in list3]
print(newlist)
