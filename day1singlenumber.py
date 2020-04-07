class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in nums:
            if nums.count(i) == 1:
                return i


def main():
    nums = [2, 2, 1]

    foo = Solution()
    print(foo.singleNumber(nums))


if __name__ == "__main__":
    main()
