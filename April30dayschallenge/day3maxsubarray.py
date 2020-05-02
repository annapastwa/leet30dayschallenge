class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # msum = nums[0]
        # # first loop
        # for i in range(len(nums) + 1):
        #     # second loop
        #     for j in range(i + 1, len(nums) + 1):
        #         # slice the subarray
        #         sub = nums[i:j]
        #         if sum(sub) > msum:
        #              msum = sum(sub)
        # return msum
        size = len(nums)
        max_so_far = nums[0]
        curr_max = nums[0]

        for i in range(1, size):
            curr_max = max(nums[i], curr_max + nums[i])
            max_so_far = max(max_so_far, curr_max)

        return max_so_far


def main():
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    foo = Solution()
    print(foo.maxSubArray(nums))


if __name__ == "__main__":
    main()