class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        return [bin(n).count('1') for n in range(num + 1)]


foo = Solution()
num = 5
print(foo.countBits(num))