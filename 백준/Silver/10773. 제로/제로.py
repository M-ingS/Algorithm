import sys
n = sys.stdin.readline
stack = []
n = int(input())
total = 0
for i in range(n):
    k = int(input())
    if k != 0:
        stack.append(k)
    else:
        stack.pop()
print(sum(stack))


