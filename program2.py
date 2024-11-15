def decode_message( s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        
        for i in range(1, n + 1):
                if p[i - 1] == '*':
                        dp[i][0] = dp[i - 1][0]
                else:
                        break

        for i in range(1, n + 1):
                for j in range(1, m + 1):
                        if p[i - 1] == s[j - 1] or p[i - 1] == '?':
                                dp[i][j] = dp[i - 1][j - 1]
                        elif p[i - 1] == '*':
                                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        return dp[n][m]

# write your code here
  
        