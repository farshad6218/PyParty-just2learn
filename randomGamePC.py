import random

print("you 1st,(1 ~ 99) ...........")
print('l for larger')
print('s for smaller')
print('w for win')
print('')

a=1
b=99
g = random.randint(a,b)
print(g)
response  = input('OK?')

while (response != 'w'):
    if(response == 'l'):
        a=g+1
        g = random.randint(a,b)
    elif(response == 's'):
        b=g-1
        g = random.randint(a,b)
    print(g)
    response  = input('OK?')

print('I win !!!!!1')