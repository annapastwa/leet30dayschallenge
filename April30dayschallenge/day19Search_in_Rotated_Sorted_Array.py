class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Time Complexity: O(n)
        if target in nums:
            return nums.index(target)
        else:
            return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 3

foo = Solution()
print(foo.search(nums, target))


# TODO: Time Complexity: O(log n):
#
# 1) Find middle point mid = (low + high)/2
# 2) If key is present at middle point, return mid.
# 3) Else If num[low..mid] is sorted
#      a) If key to be searched lies in range from num[low] to num[mid], recursion for num[low..mid].
#      b) Else recursion for num[mid+1..high]
# 4) Else (num[mid+1..high] must be sorted)
#      a) If key to be searched lies in range from num[mid+1] to num[high], recursion for num[mid+1..high].
#      b) Else recursion for num[low...mid]

