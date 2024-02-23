import sys
input = sys.stdin.readline

def DFS(depth, total, pl, mi, mu, di):
    global maxi, mini
    if depth == n:
        maxi = max(total, maxi)
        mini = min(total, mini)
        return
    if pl:
        DFS(depth + 1, total + num[depth], pl - 1, mi, mu, di)
    if mi:
        DFS(depth+1, total-num[depth], pl, mi-1, mu, di)
    if mu:
        DFS(depth+1, total*num[depth], pl, mi, mu-1, di)
    if di:
        DFS(depth+1, int(total/num[depth]), pl, mi, mu, di-1)


n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))
maxi = -1e9
mini = 1e9
DFS(1, num[0], op[0], op[1], op[2], op[3])
print(maxi)
print(mini)
# 2    n
# 5 6   num
# 0 0 1 0   op
# + - * %