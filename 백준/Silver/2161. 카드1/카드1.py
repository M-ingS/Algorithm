from collections import deque
import sys
input = sys.stdin.readline
dq = deque([])
k = []
n = int(input())    # dq = [1, 2, 3, 4]
for i in range(1, n+1): #dq = [i for i in range(1, n+1)]
    dq.append(i)

while len(dq) != 1:
    k.append(dq.popleft())
    dq.append(dq.popleft())
k.append(str(dq[0]))  # 마지막 남은 값 추가

for i in k:
    print(i, end=' ')