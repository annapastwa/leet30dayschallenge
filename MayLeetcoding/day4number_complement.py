# Number Complement
# Given a positive integer, output its complement number.
# The complement strategy is to flip the bits of its binary representation.
# Note:
# The given integer is guaranteed to fit within the range of a 32-bit signed integer.
# You could assume no leading zero bit in the integer’s binary representation.
# This question is the same as 1009: https://leetcode.com/problems/complement-of-base-10-integer/


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int('0b' + "".join("1" if i == "0" else "0" for i in bin(num)[2:]), 2)
        # return ((1 << num.bit_length()) - 1) ^ num # bitwise flipping alternative


n = 5  # for 5 return 2, for 1 return 0
foo = Solution()
print(foo.findComplement(n))
