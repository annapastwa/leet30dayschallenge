class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        if len(text1) == 0 or len(text2) == 0:
            return 0

        m = len(text1)
        n = len(text2)
        memo = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        #print(memo)

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if text1[row - 1] == text2[col - 1]:
                    memo[row][col] = 1 + memo[row - 1][col - 1]
                else:
                    memo[row][col] = max(memo[row][col - 1], memo[row - 1][col])
        #print(memo)
        return memo[m][n]


text1 = "oxcpqrsvwf"
text2 = "shmtulqrypy"

foo = Solution()
print(foo.longestCommonSubsequence(text1, text2))
