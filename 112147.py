n = float(input())
s=1
for i in range(0, 10):
  s = s*n
if int(s)==s:
  print(float(s), 0, 0, sep="")
else:
  print(round((s), 3))