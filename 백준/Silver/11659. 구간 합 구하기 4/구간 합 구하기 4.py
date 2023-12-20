import sys
input = sys.stdin.readline
nn, m = map(int, input().split())
n = list(map(int, input().split()))
# n = [5 4 3 2 1]       합 배열: s = s[i-1] + n[i]
# s = [0 5 9 12 14 15]
#합 배열 생성
s = [0] * (nn+1)
for i in range(1, nn+1):  #인덱스 1부터 5(n의길이 0~4)까지 합 배열 s를 생성
    s[i] = s[i-1] + n[i-1]
# print(len(s))
#구간 합   ex) i=1 j=3
for k in range(m):     # ex) k=0 ~ m(m=3)까지 3번 돌림. 구간 합 구하는 것을.
    i, j = map(int, input().split())
    g = s[j] - s[i-1]
    print(g)
