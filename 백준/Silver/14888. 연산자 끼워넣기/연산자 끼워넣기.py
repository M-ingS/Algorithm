import sys
input = sys.stdin.readline
# depth: 현재까지 쓴 숫자 갯수, total: 현재까지 계산 결과, 각 연산자는 남은 각 연산자의 개수
def DFS(depth, total, plus, minus, mul, div):
    global maximum, minimum
    if depth == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return
    if plus:    # plus의 개수가 남았다면
        DFS(depth+1, total+num[depth], plus-1, minus, mul, div)
    if minus:
        DFS(depth+1, total-num[depth], plus, minus-1, mul, div)
    if mul:
        DFS(depth+1, total*num[depth], plus, minus, mul-1, div)
    if div:
        DFS(depth+1, int(total/num[depth]), plus, minus, mul, div-1)

n = int(input())
num = list(map(int, input().split()))     # 수열
op = list(map(int, input().split()))     # 각 연산자 개수
maximum = -1e9
minimum = 1e9
DFS(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)
# 2    n
# 5 6   num
# 0 0 1 0   op
# + - * %