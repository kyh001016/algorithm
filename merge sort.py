import random

array = []
for i in range(20):
    a = random.randint(1,100)
    while a in array:
        a = random.randint(1,100)
    array.append(a)
print(array)

def merge_sort(array):
    def sort(low, high):
        if high - low < 2:
            return
        mid = (low + high) // 2
        sort(low, mid)
        sort(mid, high)
        merge(low, mid, high)

    def merge(low, mid, high):
        temp = []
        l, h = low, mid

        while l < mid and h < high:
            if array[l] < array[h]:
                temp.append(array[l])
                l += 1
            else:
                temp.append(array[h])
                h += 1

        while l < mid:
            temp.append(array[l])
            l += 1
        while h < high:
            temp.append(array[h])
            h += 1

        for i in range(low, high):
            array[i] = temp[i - low]

    return sort(0, len(array))

merge_sort(array)
print(array)
