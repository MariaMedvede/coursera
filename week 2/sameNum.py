a, b, c = int(input()), int(input()), int(input())
count = 0
if a == b:
    count += 1
if a == c:
    count += 1
if b == c:
    count += 1
if count == 1:
    count += 1
print(count)
