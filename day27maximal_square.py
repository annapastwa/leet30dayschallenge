class Solution(object):
    def maximalSquare(self, matrix):
        """
        Given a 2D array of 0 and 1, find the largest square of 1's and return its area.
        :param matrix: List[List[str]]
        :return: int
        """
        # define deepest point at r,c by replacing matrix values: bruteforce apprach
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        #print(dp)
        area = 0

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r == 0 or c == 0: # if border, then max is 1 to arrive there
                    dp[r][c] = int(matrix[r][c])
                elif int(matrix[r][c]) == 1: # check left, top, left-top
                    dp[r][c] = min(dp[r - 1][c - 1], dp[r][c - 1], dp[r - 1][c]) + 1 # all must be 1
                area = max(area, dp[r][c])
        #print(dp)

        return area * area


if __name__ == "__main__":
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    foo = Solution()
    print(foo.maximalSquare(matrix))
