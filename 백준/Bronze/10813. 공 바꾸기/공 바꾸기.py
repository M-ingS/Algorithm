import sys
input = sys.stdin.readline
n, m = map(int, input().split())

basket = [0] * (n+1)
for i in range(1, n+1):
    basket[i] = i

for z in range(m):
    i, j = map(int, input().split())
    temp = 0
    temp = basket[i]
    basket[i] = basket[j]
    basket[j] = temp

for i in range(1, n+1):
    print(basket[i], end=' ')