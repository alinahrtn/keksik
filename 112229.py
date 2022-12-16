numb = int(input())

m = {1}
sumlist = 1
i = 2
while i * i <= numb and sumlist <= numb:
    if (numb % i == 0):
        sumlist += i + (numb // i if i != numb // i else 0)
        m.update({i, numb // i})
    i += 1

if sumlist == numb:
    print(*sorted(m))
else:
    print(0)