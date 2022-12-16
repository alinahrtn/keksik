def bSort(array):
    length = len(array)
    sr=0
    p=0
    for i in range(length):
        for j in range(length-1):
            if array[j] > array[j+1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                p=p+1
                sr = sr + 1
            else:
                sr = sr + 1
    print(p)