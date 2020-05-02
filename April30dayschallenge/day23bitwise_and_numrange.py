class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        i = 0
        while m < n:
            m = m >> 1
            n = n >> 1
            i += 1
        return m << i


foo = Solution()
print(foo.rangeBitwiseAnd(5, 7))
