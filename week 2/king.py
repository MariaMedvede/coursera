# Шахматный король ходит по горизонтали, вертикали и диагонали,
# но только на 1 клетку.
# Даны две различные клетки шахматной доски,
# определите, может ли король попасть
# с первой клетки на вторую одним ходом.
A1 = int(input())
A2 = int(input())
B1 = int(input())
B2 = int(input())
if abs(B1 - A1) <= 1 and abs(B2 - A2) <= 1:
    print("YES")
else:
    print("NO")
