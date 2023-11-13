import random
r = random.randint(1 , 99)
g = int(input('Guess 1 ~ 99?'))
while r != g:
    if(r>g):
        print("random is larger")
    else:
        print("random is smaller")
    g = int(input('Guess 1 ~ 99?'))

print('You Win !!!')


