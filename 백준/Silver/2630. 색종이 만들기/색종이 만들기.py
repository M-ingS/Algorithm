def dfs(x, y, n):
    global white, blue
    visited = paper[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != visited:  # 색이 하나라도 다르면 4등분
                dfs(x, y, n//2)      # 좌상단
                dfs(x, y+n//2, n//2) # 우상단
                dfs(x+n//2, y, n//2) # 좌하단
                dfs(x+n//2, y+n//2, n//2) #우하단
                return
    if visited == 0:
        white += 1
    else:
        blue += 1

n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]
white, blue = 0, 0
dfs(0, 0, n)
print(white)
print(blue)