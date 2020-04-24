class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # counter = 0
        # csum = 0
        #
        # if len(nums) < 1:
        #     return counter
        #
        # for i in range(len(nums)):
        #     csum = 0
        #     for j in range(i, len(nums)):
        #
        #         csum += nums[j]
        #         print("i: {} j: {} csum: {} counter: {}".format(i, j, csum, counter))
        #         if csum == k:
        #             counter += 1
        #         #     break
        #         # elif csum > k:
        #         #     break
        #
        # return counter

        count = 0
        for start in range(len(nums)):
            sum=0
            for end in range(start, len(nums)):
                sum += nums[end]
                if (sum == k):
                    count +=1


        return count

# Complexity Analysis
# Time complexity : O(n^2)O(n2). We need to consider every subarray possible.
# Space complexity : O(1)O(1). Constant space is used.



nums = [0,0,0,0,0,0,0,0,0,0]
# [28,54,7,-70,22,65,-6] 100

# [100,1,2,3,4] 6
# [1, 2, 3] 3
# [1, 1, 1] 2

k = 0

foo = Solution()
print(foo.subarraySum(nums, k))

# Alternative
# class Solution:
#     def subarraySum(self, nums, k):
#         preSums = {0: 1}
#         s = 0
#         result = 0
#         for i in nums:
#             s += i
#             result += preSums.get(s - k, 0)
#             preSums[s] = preSums.get(s, 0) + 1
#         return result
