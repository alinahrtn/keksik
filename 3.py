list = input().split()
list = [46, 29, 14, 10, 30]
for beg in range(len(list)-1):
    localMax = max(list[beg+1:len(list)])
    if localMax <= list[beg]:
        continue
    localMaxIndex = list.index(localMax)
    list[beg], list[localMaxIndex] = list[localMaxIndex], list[beg]
list.reverse()
print(list)