class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid or len(grid) == 0:
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i > 0 and j > 0:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                elif i > 0:
                    grid[i][j] += grid[i - 1][j]
                elif j > 0:
                    grid[i][j] += grid[i][j - 1]
                # print(i, j, grid[i][j])
        return grid[-1][-1]


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

foo = Solution()
print(foo.minPathSum(grid))
