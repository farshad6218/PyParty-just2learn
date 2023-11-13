a = [(1,5),(5,2),(3,9),(2,7),(4,3)]
print(a)

a.sort()
print(a)

a.sort(key= lambda x:x[1])
print(a)

# map
myList = [2,4,6,8,1,3,5,7]
MyNewList = map(lambda x : x*2 , myList)
print(*MyNewList)

# filter
MyNewList2 = filter(lambda x : x % 2 == 0 , myList)
print(*MyNewList2)
