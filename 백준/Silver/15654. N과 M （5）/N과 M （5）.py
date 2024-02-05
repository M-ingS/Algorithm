N, M = map(int, input().split())
m = list(map(int, input().split()))
a = sorted(m)
s = []
def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return
    for i in a:
        if i not in s:
            s.append(i)
            dfs()
            s.pop()
dfs()
