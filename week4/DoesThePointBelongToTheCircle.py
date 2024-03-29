import math


def IsPointInCircle(x, y, xc, yc, r):
    return math.sqrt((xc - x)**2 + (yc - y)**2) <= r


x1 = float(input())
y1 = float(input())
xc1 = float(input())
yc1 = float(input())
r1 = float(input())

if IsPointInCircle(x1, y1, xc1, yc1, r1):
    print("YES")
else:
    print("NO")
