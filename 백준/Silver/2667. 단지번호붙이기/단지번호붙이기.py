from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    g[x][y] = 0 # 방문한 곳을 0으로 하여 다시 방문x
    cnt = 1     #넓이(집의 개수)

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while q:
        x, y = q.popleft()
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0<=a<n and 0<=b<n and g[a][b] == 1:  # 입력받은 범위 안 + 값이 1이면
                q.append((a, b))
                g[a][b] = 0
                cnt += 1    # 집의 개수 1증가
    return cnt

n = int(input()) # 가로 = 세로 크기
g = [] # 지도
result = [] # 단지의 수들을 저장할 리스트
for _ in range(n):
    a = list(map(int, input()))
    g.append(a)

# 모든 위치에 대해 BFS 수행
for i in range(n):
    for j in range(n):
        if g[i][j] == 1:    # 1이면 bfs수행 후 result리스트에 단지 별 집 개수를 추가
            result.append(bfs(i, j))

print(len(result))
result.sort()
for i in result:    # 오름차순 후 출력
    print(i)