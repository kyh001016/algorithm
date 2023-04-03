import random

array = []
for i in range(20):
    a = random.randint(1,100)
    while a in array:
        a = random.randint(1,100)
    array.append(a)
print(array)

def insertion_sort(array):
    for end in range(1, len(array)):
        for i in range(end, 0, -1):
            if array[i - 1] > array[i]:
                array[i - 1], array[i] = array[i], array[i - 1]

insertion_sort(array)
print(array)
