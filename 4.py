s = input()
arr1 = input().split()
arr2 = input().split()
for x in arr2:
    print(('NO','YES')[bool(arr1.count(x))])