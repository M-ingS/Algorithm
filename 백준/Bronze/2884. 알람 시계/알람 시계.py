H, M = map(int, input().split())

if M - 45 >= 0:     # 분이 0이상일 때
    print(H, M - 45, end=' ')

else:       # 분이 0보다 작아질 때
    if H == 0:   # ex) 0시 15분 - 45분 = 23시 30분
        print(H + 23, (60 + M) - 45, end=' ')
    else:       # ex) 11시 15분 - 45분 = 10시 30분
        print(H - 1, (60 + M) - 45, end=' ')