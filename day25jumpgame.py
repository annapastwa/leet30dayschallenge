class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Dynamic programming task, greedy approach
        dtt = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= dtt:
                dtt = i
        return dtt == 0

# Complexity Analysis
# Time complexity : O(n)O(n). We are doing a single pass through the nums array,
# hence nn steps, where nn is the length of array nums.
# Space complexity : O(1)O(1). We are not using any extra memory.


nums = [2, 3, 1, 1, 4]
foo = Solution()
print(foo.canJump(nums))
