n, m = map(int, input().split())
a = list(map(int, input().split()))
l = sorted(a)
s = []
def b_t():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in l:
        s.append(i)
        b_t()
        s.pop()
b_t()