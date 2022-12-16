n = int(input())
k = 0
d = -1
while n > 0:
    if n % 10 == d:
        k = 1
    d = n % 10
    n = n // 10
if k == 1:
    print("YES")
else:
    print("NO")