string =   "Salam, This is Farshad and testing Python"

counter = dict()

for letter in string:
    counter[letter] = counter.get(letter,0) + 1
    # if letter in counter:
    #     counter[letter] += 1
    # else:
    #     counter[letter]  = 1
    # print(letter,counter)


# print(counter)

for c in list(counter.keys()):
    print('\"%s\" --> %s time ' % (c,counter[c]))

