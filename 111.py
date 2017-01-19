import random

dish = input('What would you like? \n').split(',')

stp = [el.strip() for el in dish]

list_dish = list(set(stp))

rand = [random.randint(1,60) for vol in  range(len(list_dish))]

i = 0

for el in list_dish:

    cap = str(el).capitalize()

    print (cap + '.......' + str(rand[i]) + 'min')

    i=i+1
