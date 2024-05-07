n, m = map(int, input().split())
basket = [0] * (n+1)

for i in range(m):
    i, j, k = map(int, input().split())
    for x in range(i, j+1):
        basket[x] = k

for i in range(1, n+1):
    print(basket[i], end=' ')