class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """

        freq = {i:s.count(i) for i in set(s)}
        sorted_x = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
        return ''.join(tuple[0] * tuple[1] for tuple in sorted_x)

s = "tree"
foo = Solution()
print(foo.frequencySort(s))