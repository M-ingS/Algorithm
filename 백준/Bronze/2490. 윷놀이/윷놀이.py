# 도: 0 1 1 1 - A
# 개: 0 0 1 1 - B
# 걸: 0 0 0 1 - C
# 윷: 0 0 0 0 - D
# 모: 1 1 1 1 - E
for i in range(3):
    n = list(map(int, input().split()))
    cnt = 0
    for i in n:
        if i == 1:
            cnt = cnt + 1
    if cnt == 0:
        print('D')  # 윷
    elif cnt == 1:
        print('C')  # 걸
    elif cnt == 2:
        print('B')  # 개
    elif cnt == 3:
        print('A')  # 도
    else:
        print('E')  # 모
# yut = [i for i in range(0, 2)]
# cnt = [0] * 4
