class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[0 for _ in range(len(text1))] for __ in range(len(text2))]
        # row: text2
        # column: text1
        for i in range(len(text2)): #row
            for j in range(len(text1)): #column
                if text2[i] == text1[j]:
                    memo[i][j] = max(1+memo[i-1][j-1] if j and i else 1, memo[i][j-1] if j else 0, memo[i-1][j] if i else 0)
                else:
                    memo[i][j] = max(memo[i-1][j] if i else 0, memo[i][j-1] if j else 0)
        return memo[len(text2)-1][len(text1)-1]