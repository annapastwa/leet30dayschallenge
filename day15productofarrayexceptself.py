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


if __name__ == '__main__':
    main()
