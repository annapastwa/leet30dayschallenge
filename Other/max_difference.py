# Max Difference You Can Get From Changing an Integer
# User Accepted:2936
# User Tried:3437
# Total Accepted:2979
# Total Submissions:7555
# Difficulty:Medium
# You are given an integer num. You will apply the following steps exactly two times:
#
# Pick a digit x (0 <= x <= 9).
# Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
# Replace all the occurrences of x in the decimal representation of num by y.
# The new integer cannot have any leading zeros, also the new integer cannot be 0.
# Let a and b be the results of applying the operations to num the first and second times, respectively.
#
# Return the max difference between a and b.

class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        low = 0
        high = 0

        if str(num)[0] != "9":
            stor = str(num)[0]
            high = int("".join(["9" for n in str(num) if n == stor]))

        return high - low


num = 555
foo = Solution()
print(foo.maxDiff(num))
