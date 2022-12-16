str = input()
arr = str.split()
arr = arr[-1:] + arr[:-1]
print(' '.join(arr))