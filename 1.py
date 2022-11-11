#1
#str = input()
#arr = str.split()
#arr = arr[-1:] + arr[:-1]
#print(arr)

#2
str = input()
list = str.split()
set = set(list)
print(len(set))

#3
#def most_frequent(List):
#    return max(set(List), key = List.count)
#
#print(most_frequent(input().split()))

#4
#input() #игнорирую бесполезный ввод первого числа
#print(input().split().count(input()))

#5
#input() #игнорирую бесполезный ввод первого числа
#print(('NO','YES')[input().split().count(input())])

#6
#s = input() #игнорирую бесполезный ввод первого числа
#arr1 = input().split()
#arr2 = input().split()
#for x in arr2:
#    print(('NO','YES')[bool(arr1.count(x))]) 

#7
#import math
#print(math.ceil(math.log2(int(input()))))

#8
#list = input().split()
#list = [46, 29, 14, 10, 30]
#for beg in range(len(list)-1):
#    localMax = max(list[beg+1:len(list)])
#    if localMax <= list[beg]:
#        continue
#    localMaxIndex = list.index(localMax)
#    list[beg], list[localMaxIndex] = list[localMaxIndex], list[beg]
#list.reverse()
#print(list)
        

#9
#data = [i for i in range(1, 51)]
#print(data)

#data = [i for i in reversed(range(1, 51))]
#print(data)

#data = [i for i in range(1, 122,3)]
#print(data)

#data = [i for i in reversed(range(1, 122))]
#print(data)

#data = [(i**2)*((-1)**((i+1)%2)) for i in range(1, 11)]
#print(data)

#s = 1
#list = [2]
#for i in range(0,10):
#    list.append(list[i]+s)
#    s=s+1
#print(list)

#list = [1,6]
#for i in range(0,9,1):
#    if i%2==0:
#        list.append(list[i]+2)
#    else:
#        list.append(list[i]+6)
#print(list)

#list = [1]
#v = 1
#for i in range(0,8,1):
#    if i%2==0:
#        list.append(list[i]+v)
#    else:
#        list.append(list[i]*v)
#        v=v+1
#print(list)