T = int(input())

for i in range(T):
    n = int(input())
    cloth = {}

    for j in range(n):
        type = list(input().split())

        if type[1] in cloth:
            cloth[type[1]].append(type[0])  # 옷의 종류(type[1])에 옷이름(type[0]) 추가
        else:
            cloth[type[1]] = [type[0]]

    cnt = 1

    for k in cloth:
        cnt *= (len(cloth[k]) + 1)  # +1:의상을 하나도 선택하지 않는 경우
    print(cnt - 1)  # 모든 의상을 선택하지 않는 경우는 제외

# {'headgear': ['hat', 'turban'], 'eyewear': ['sunglasses']}
# headgear: 3가지 (hat, turban 중 하나를 선택하거나 아무것도 선택하지 않는 경우)
# eyewear: 2가지 (sunglasses를 선택하거나 선택하지 않는 경우)
# cnt = 1 * 3 * 2 = 6
# 최종 결과: 6 - 1 = 5 가지 조합(최종적으로 아무 것도 착용하지 않는 경우를 제외)

# {'face': ['mask', 'sunglasses', 'makeup']}
# face: 4가지 (mask, sunglasses, makeup 중 하나를 선택하거나 아무것도 선택하지 않는 경우)
# cnt = 1 * 4 = 4
# 최종 결과: 4 - 1 = 3 가지 조합