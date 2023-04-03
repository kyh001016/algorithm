import random

array = []
for i in range(20):
    a = random.randint(1,100)
    while a in array:
        a = random.randint(1,100)
    array.append(a)
print(array)

def heap_sort(array):
    n = len(array)
    # heap 구성
    for i in range(n):
        c = i
        while c != 0:
            r = (c-1)//2
            if (array[r] < array[c]):
                array[r], array[c] = array[c], array[r]
            c = r
            
    # 크기를 줄여가면서 heap 구성
    for j in range(n-1, -1, -1):
        array[0] , array[j] = array[j], array[0]
        r = 0
        c = 1
        while c<j:
            c = 2*r +1
            # 자식 중 더 큰 값 찾기
            if (c<j-1) and (array[c] < array[c+1]):
                c += 1
            # 루트보다 자식이 크다면 교환
            if (c<j) and (array[r] < array[c]):
                array[r], array[c] = array[c], array[r]
            r=c
    print(array)
            

heap_sort(array)
