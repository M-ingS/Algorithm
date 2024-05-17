t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    if a + b >= 24:
        print(f'#{i+1} {a + b - 24}')
    else:
        print(f'#{i+1} {a+b}')
