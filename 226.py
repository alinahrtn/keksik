input()
list = input().split()
val = input()
list2 = []
for x in range(len(list)):
    if list[x] == val:
        list2.append(str(x+1))
print(' '.join(list2))