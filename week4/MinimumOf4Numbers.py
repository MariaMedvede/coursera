def min4(a, b, c, d):
    return min(min(a, b), min(c, d))


a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())

print(min4(a1, a2, a3, a4))
