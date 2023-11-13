t = (1,3,5, 'Hi')
print( type(t) )

a,b = 'asd@gmail.com'.split('@')
print(a,b)

print('-----------------')

# dictionary
weight = {'Farshad' : 74,'Kourosh': 40 ,'Sahra' : 53}
d  = weight.items()
print(d)

print()
print()
print()


l = list(weight.items())
print(l)

print()
print()
print()

for name , name_weight in l:
    # print(name,' =',name_weight)
    print('%s = %s' % (name,name_weight))
