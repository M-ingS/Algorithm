import sys
input = sys.stdin.readline
cnt = 0
n = int(input())
for i in range(n):
    data = input().strip()
    s = []
    for i in data:
        if s and s[-1] == i: #스택이 비어있지x,맨 위 글자와 현재 글자가 같으면
            s.pop()
        else:
            s.append(i)
    if not s: #스택이 비어있지 않으면 좋은단어 + 1
        cnt += 1
print(cnt)