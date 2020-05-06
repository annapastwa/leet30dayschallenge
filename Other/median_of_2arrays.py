# 4. Median of Two Sorted Arrays
# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        nums3 = sorted(nums1 + nums2)

        if len(nums3) % 2 == 0:
            return (nums3[len(nums3) // 2 - 1] + nums3[len(nums3) // 2]) / 2
        else:
            return nums3[len(nums3) // 2]


nums1 = [1, 2]
nums2 = [3, 4]
foo = Solution()
print(foo.findMedianSortedArrays(nums1, nums2))
