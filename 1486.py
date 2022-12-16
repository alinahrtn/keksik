import math
a = int(input())
a1 = a//1000
a2 = (a//100)%10
a3= (a%100)//10
a4 = a%10
b1 = abs(a1-a2)
b2 = abs(a1-a3)
b3 = abs(a1-a4)
b4 = abs(a2-a3)
b5 = abs(a2-a4)
b6 = abs(a3-a4)
c1=b1+b2
c2=b1+b3
c3=b1+b4
c4=b1+b5
c5=b1+b6
c6=b2+b3
c7=b2+b4
c8=b2+b5
c9=b2+b6
c10=b3+b4
c11=b3+b5
c12=b3+b6
c13=b4+b5
c14=b4+b6
c15=b5+b6
#s = abs(((min(b1, b2, b3, b4, b5, b6)-min(b1, b2, b3, b4, b5)+min(b1, b2, b3, b4)-min(b1, b2, b3)+min(b1, b2)-b1)))

m =  min(c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15)
m1 = (m/float(m+1))
m2 = int(-1 * m1 // 1 * -1)
m3 = 1 - m2
s = 1 + min(b1,b2,b3,b4,b5,b6) + 228*m3
print(s)