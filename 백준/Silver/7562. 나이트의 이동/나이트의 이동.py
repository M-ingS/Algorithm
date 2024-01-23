from collections import deque

def BFS(a1, b1, a2, b2):
    q = deque()
    q.append((a1, b1, 0))    # 시작 위치, 이동 횟수 0을 함께 큐에 추가
    visited[a1][b1] = True
    #방향 벡터
    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    while q:
        x, y, cnt = q.popleft()  #현재 위치 꺼냄
        if x == a2 and y == b2:  #목표 위치에 도달하면 이동 횟수 반환
            return cnt
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                q.append((nx, ny, cnt + 1)) # 이동 횟수를 1증가시켜서 큐에 추가
                visited[nx][ny] = 1

T = int(input())
for i in range(T):
    n = int(input())
    a1, b1 = map(int, input().split())    # 나이트의 위치
    a2, b2 = map(int, input().split())    # 목표 위치
    visited = [[False] * n for _ in range(n)]
    print(BFS(a1, b1, a2, b2))