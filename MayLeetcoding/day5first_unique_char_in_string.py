# First Unique Character in a String
# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
# Examples:
# s = "leetcode"
# return 0.
# s = "loveleetcode",
# return 2.
# Note: You may assume the string contain only lowercase letters.

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        for i, el in enumerate(s):
            if s.count(el) == 1:
                return i
        return -1

        # # Build hash map : character and how often it appears
        # count = collections.Counter(s)
        #
        # # find the index
        # for idx, ch in enumerate(s):
        #     if count[ch] == 1:
        #         return idx
        # return -1

        # Clever fast for Python
        # letters='abcdefghijklmnopqrstuvwxyz'
        # index=[s.index(l) for l in letters if s.count(l) == 1]
        # return min(index) if len(index) > 0 else -1

s = "loveleetcode"
foo = Solution()
print(foo.firstUniqChar(s))
