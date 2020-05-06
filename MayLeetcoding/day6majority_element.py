# Majority Element
# Given an array of size n, find the majority element.
# The majority element is the element that appears more than ⌊ n/2 ⌋ times.
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Example 1:
# Input: [3,2,3]
# Output: 3
# Example 2:
# Input: [2,2,1,1,1,2,2]
# Output: 2

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in set(nums):
            if nums.count(i) > len(nums) // 2:
                return i

        # # Hashmap
        # counts = collections.Counter(nums)
        # return max(counts.keys(), key=counts.get)
        #
        # # Sorting - using the > n/2 property
        # nums.sort()
        # return nums[len(nums)//2]


nums = [2, 2, 1, 1, 1, 2, 2]
foo = Solution()
print(foo.majorityElement(nums))
