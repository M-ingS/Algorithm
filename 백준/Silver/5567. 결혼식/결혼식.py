from collections import deque

def BFS(start):
    # 시작 노드랑 연결된 친구가 없는 경우
    if not list[start]:
        print(0)
        return

    q = deque()
    q.append(start)
    visited[start] = True
    cnt = 0     # 초대할 사람이 몇 명인지
    depth = 0   # 깊이가 2이면 끝(친구의 친구까지)

    while q:
        depth += 1
        for _ in range(len(q)):
            x = q.popleft()

            for i in list[x]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
                    cnt += 1
        if depth == 2:
            print(cnt)
            break


n = int(input())
m = int(input())
list = [[] for _ in range(n+1)]
visited = [False] * (n+1)

#양방향 그래프로 연결
for _ in range(m):
    a, b = map(int, input().split())
    list[a].append(b)
    list[b].append(a)

BFS(1)