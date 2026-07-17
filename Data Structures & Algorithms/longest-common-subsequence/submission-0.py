class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        memo = [[0]*(m+1) for _ in range(n+1)]
        # for i in range(n):
        #     memo[i+1][0] = i+1
            
        # for j in range(m):
        #     memo[0][j+1] = j+1

        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    print(text1[i-1], text2[j-1])
                    memo[i][j] = memo[i-1][j-1]+1
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])
        for row in memo:
            print(row)
        return memo[n][m]