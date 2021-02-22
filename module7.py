#itertools
import itertools

#infinite iterators
for i in itertools.count(1,2):
    if i == 11:
        break
    else:
        print(i)

#itertools cycle

count = 0

for i in itertools.cycle("Hello"):
    if count > 10:
        break
    else:
        print(i)
        count += 1

#itertools repeat
number = int(input("What number would you like to be repeated:"))
times = int(input("How many times would you like to repeated it:"))

print(list(itertools.repeat(number, times)))

#copy
import copy

names = ["Sarah","Peter","Jack"]

#shallow copy
namesShallow = copy.copy(names)
print(namesShallow)

#deep copy
namesDeep = copy.deepcopy(names)
print(namesDeep)
