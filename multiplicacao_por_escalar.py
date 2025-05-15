x, y = map(int, input().split())
n = 0
for i in range (y+1, x-1):
    if i % 2 != 0:
        n += i
print(n)


