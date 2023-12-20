import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[0] * (n+1)] #1차원 리스트
D = [[0] * (n+1) for _ in range(n+1)] # 2차원 리스트

for i in range(n):  #1행으로 만들어진 리스트를 n개만큼 반복해서 2차원 배열생성
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)
#합 배열 D
for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]
#합 배열을 이용하여 질의에 대한 결과 구하기기for _ in range
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)