a, b, c = map(int, input().split())
s = a+b+c
pr = a*b*c
sr = (a+b+c)/3
print(a, "+", b, "+", c, "=", s, sep="")
print(a, "*", b, "*", c, "=", pr, sep="")
if int(sr)==sr:
  print("(", a, "+", b, "+", c, ")", "/3",  "=", round(sr, 3), 0, 0, sep="")
else:
  print("(", a, "+", b, "+", c, ")", "/3",  "=", round(sr, 3), sep="")