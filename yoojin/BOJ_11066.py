import sys
read = sys.stdin.readline

t = int(read())
for _ in range(t):
    n = int(read())
    files = list(map(int, read().split()))
    dp = [[0] * (n) for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + sum(files[i:j + 1]))

    print(dp[0][n - 1])