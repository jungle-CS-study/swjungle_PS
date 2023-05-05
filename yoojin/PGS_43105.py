def solution(triangle):
    answer = 0
    dp = list([0] * len(triangle) for j in range(len(triangle)))
    # t[level][elem] = max(t[level-1][elem-1], t[level-1][elem])
    dp[0][0] = triangle[0][0]
    for i in range(1, len(triangle)):
        for j in range(0, len(triangle[i])):
            if j == 0 or j == len(triangle[i]) - 1:
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1] + triangle[i][j], dp[i-1][j] + triangle[i][j])
    answer = max(dp[len(triangle)-1])
    return answer
