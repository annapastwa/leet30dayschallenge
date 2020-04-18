class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        # if not grid:
        #     return 0
        #
        # def sink_island(i, j):
        #     if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
        #         grid[i][j] = '0'
        #         list(map(sink_island, (i + 1, i - 1, i, i), (j, j, j + 1, j - 1)))  # map in python3 return iterator
        #         return 1
        #     return 0
        #
        # return sum(sink_island(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

        # Alternative recursion

        if not grid: return 0
        R, C = len(grid), len(grid[0])

        def sink_island(r, c):
            if 0 <= r < R and 0 <= c < C and grid[r][c] == "1":
                grid[r][c] = "0"
                sink_island(r + 1, c)
                sink_island(r - 1, c)
                sink_island(r, c + 1)
                sink_island(r, c - 1)

        island = [sink_island(r, c) for r in range(R) for c in range(C) if grid[r][c] == "1"]
        return len(island)


grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
foo = Solution()
print(foo.numIslands(grid))
