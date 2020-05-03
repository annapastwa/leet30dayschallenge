# Ransom Note
# Given an arbitrary ransom note string and another string containing letters from all the magazines,
# write a function that will return true if the ransom note can be constructed from the magazines ;
# otherwise, it will return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
#
# Note:
# You may assume that both strings contain only lowercase letters.

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        note = {n: ransomNote.count(n) for n in set(ransomNote)}

        for n in note:
            if n not in magazine or magazine.count(n) < note[n]:
                return False
        return True

        # Can be effectively reduced to:
        # for n in set(ransomNote):
        #     if ransomNote.count(n) > magazine.count(n):
        #         return False
        # return True

        # or to a slower one-liner:
        # return not collections.Counter(ransomNote) - collections.Counter(magazine)


ransomNote = "aa"
magazine = "ab"
foo = Solution()
print(foo.canConstruct(ransomNote, magazine))
