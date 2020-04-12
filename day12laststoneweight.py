class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """

        while len(stones) > 1:
            stones = sorted(stones, reverse=True)
            e = stones[0] - stones[1]
            stones = stones[2:]
            if e > 0:
                stones.append(e)

        if len(stones) > 0:
            return stones[0]
        else:
            return len(stones)


def main():
    stones = [2, 7, 4, 1, 8, 1]
    foo = Solution()
    print(foo.lastStoneWeight(stones))


if __name__ == '__main__':
    main()
