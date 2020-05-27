class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        d = {}
        d[0] = 0

        ml = 0
        sum = 0

        for i, num in enumerate(nums):
            if num == 0:
                sum -= 1
            else:
                sum += 1

            if sum in d:
                ml = max(ml, i - d[sum] + 1)
            else:
                d[sum] = i + 1
        return ml
