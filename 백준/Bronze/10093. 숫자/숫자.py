a, b = map(int, input().split())
n1 = min(a, b)
n2 = max(a, b)
n = n2 - n1 - 1
if n < 1:
    n = 0
print(n)
for i in range(n1, n2):
    n1 = n1 + 1
    if n1 == n2:
        continue
    print(n1, end=' ')




