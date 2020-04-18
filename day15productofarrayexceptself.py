class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        leftprod = [1]
        rightprod = [1]
        oprod = []

        for i in range(len(nums) - 1):
            lprod = leftprod[i] * nums[i]
            leftprod.append(lprod)

        rnums = list(reversed(list(nums)))
        for i in range(len(nums) - 1):
            rprod = rightprod[i] * rnums[i]
            rightprod.append(rprod)

        for i in range(len(nums)):
            oprod.append(leftprod[i] * rightprod[-i - 1])

        return oprod


def main():
    nums = [1, 2, 3, 4]
    foo = Solution()
    print(foo.productExceptSelf(nums))


# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         ans = [1 for _ in nums]
#
#         left = 1
#         right = 1
#
#         for i in range(len(nums)):
#             ans[i] *= left
#             ans[-1 - i] *= right
#             left *= nums[i]
#             right *= nums[-1 - i]
#
#         return ans


if __name__ == '__main__':
    main()
