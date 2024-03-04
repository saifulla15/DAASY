def optimal_bst(keys, freq):
    n = len(keys)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = freq[i]

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            dp[i][j] = float('inf')
            for r in range(i, j + 1):
                c = dp[i][r - 1] + dp[r + 1][j] + sum(freq[i:j + 1])
                if c < dp[i][j]:
                    dp[i][j] = c

    return dp[0][n - 1]


keys = [10, 12, 20]
freq = [34, 8, 50]
print(optimal_bst(keys, freq))
