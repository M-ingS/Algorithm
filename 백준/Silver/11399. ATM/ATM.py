#인출 시간이 적은 순으로 정렬
n = int(input())    # 사람 수
l = list(map(int, input().split())) # 각 사람이 인출하는데 걸리는 시간

l.sort()
time = 0

for i in range(1, n+1):
    time += sum(l[0:i])     # 1 2 3 3 4 | 1+3+6+9+13
print(time)