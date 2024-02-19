def dfs(now, broken):
    if now == n:  # 모든 계란을 다 쳤거나 마지막 계란에 도달한 경우
        return broken

    if s[now][0] <= 0:  # 현재 계란이 이미 깨진 경우
        return dfs(now + 1, broken)  # 다음 계란으로 넘어감

    result = broken
    hit = False
    for i in range(n):
        if i != now and s[i][0] > 0:  # 자기 자신이 아니고, 안깨진 계란을 침
            hit = True
            s[now][0] -= s[i][1]
            s[i][0] -= s[now][1]

            next_broken = broken + (s[now][0] <= 0) + (s[i][0] <= 0)
            result = max(result, dfs(now + 1, next_broken))  # 다음 계란으로 이동

            s[now][0] += s[i][1]
            s[i][0] += s[now][1]

    # 현재 든 계란으로 칠 수 있는 계란이 없는 경우
    if not hit:
        result = max(result, dfs(now + 1, broken))  # 다음 계란으로 넘어감

    return result

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
print(dfs(0, 0))