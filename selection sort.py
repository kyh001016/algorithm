import random

array = []
for i in range(20):
    a = random.randint(1,100)
    while a in array:
        a = random.randint(1,100)
    array.append(a)
print(array)

def selection_sort(array):
    for i in range(len(array) - 1):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
selection_sort(array)
print(array)
