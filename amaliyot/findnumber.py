import random

def find_number(x):
    y = int(input("Sonni kiriting: "))

    n = 1

    while x != y:
        if x > y:
            y = int(input("Men o'ylagan son bundan katta: "))
            n += 1
        elif x < y:
            y = int(input("Men o'ylagan son bundan kichkina: "))
            n += 1
    return f'{n} ta urinishda topdingiz'

x = random.randint(1, 10)
print(x)
print(find_number(x))