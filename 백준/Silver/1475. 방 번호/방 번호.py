n = list(map(int, input()))
sett = [i for i in range(10)] # 0 ~ 9
sett_cnt = [0] * 10

for i in n:
    if i in sett:   #입력 받은 n의 i번째 값이 sett(0~9)안에 있다면 해당 숫자 카운트 1증가
        if (i == 6 or i == 9):
            if sett_cnt[6] <= sett_cnt[9]:
                sett_cnt[6] = sett_cnt[6] + 1
            else:
                sett_cnt[9] = sett_cnt[9] + 1
        else:
            sett_cnt[i] = sett_cnt[i] + 1
result = max(sett_cnt)
print(result)
