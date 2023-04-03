import random

array = []
for i in range(20):
    a = random.randint(1,100)
    while a in array:
        a = random.randint(1,100)
    array.append(a)
print(array)

def bubbleSort(array):
    n = len(array) # 배열의 크기를 측정

    # 배열의 크기만큼 반복
    for i in range(n):
        
        # 배열의 총 크기에서 i의 값과 1을 뺀 만큼 반복
        for j in range(0, n - i - 1):
            
            # 만약 현재 인덱스의 값이 다음 인덱스의 값보다 클경우 실행
            if array[j] > array[j + 1]: 
                array[j], array[j + 1] = array[j + 1], array[j]# 서로 위치를 변환
          
        


bubbleSort(array)
print(array)

