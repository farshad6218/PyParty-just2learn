def getNumber():
    yield 1
    yield 2
    yield 3

for i in getNumber():
    print(i)

print('----------')

def infinite_sequence(n):
    num = 0
    while num < n:
        yield num
        num += 1

for i in infinite_sequence(3):
    print(i)

print('----------')

for i in infinite_sequence(6):
    print(i)
