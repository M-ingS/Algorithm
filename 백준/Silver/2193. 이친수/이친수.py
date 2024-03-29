n = int(input())

dp = [0] * (n+1)
dp[1] = 1

for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]   # 마지막자리가 0일 경우, n-1자리는 어떤 이친수도 가능
                        # 마지막 자리가 1일 경우, 그 앞자리는 무조건 0, n-2자리는 어떤 이친수도 가능
print(dp[n])

# n=1 -> 1
# n=2 -> 10
# n=3 -> 100, 101
# n=4 -> 10 10, 10 00, 10 01
# n=5 -> 10 100, 10 101, 10 000, 10 010, 10 001
# n=4일 때, n=2 + n=3 과 같고, n=5일 때, n=3 + n=4 와 같다. (각각 뒤에 2자리, 3자리 비교)