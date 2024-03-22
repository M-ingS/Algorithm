# n: 동전 종류, k: 합
n, k = map(int, input().split())
l = []
cnt = 0
for _ in range(n):
    l.append(int(input()))

l.sort(reverse=True)
# 5만원(큰것부터)부터 나누어떨어지면 나머지 연산 아니면 다음 큰 것
for i in l:
    if i > k:   # i로 k를 나눌 수 없으면
        continue
    elif i <= k:    # k = 4200, i = 1000이면 나눠짐
        cnt += k // i
        k = k % i

print(cnt)