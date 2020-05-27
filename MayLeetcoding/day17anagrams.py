class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # Hash the number of times each character appears in p.
        # Iterate over s with a sliding window and maintain a similar hash.
        # If these two hashes are ever the same, add that to the result.
        res = []

        n, m = len(s), len(p)

        if n < m:
            return res

        phash, shash = [0] * 123, [0] * 123

        for x in p:
            phash[ord(x)] += 1

        for x in s[:m - 1]:
            shash[ord(x)] += 1

        for i in range(m - 1, n):
            shash[ord(s[i])] += 1
            if i - m >= 0:
                shash[ord(s[i - m])] -= 1
            if shash == phash:
                res.append(i - m + 1)

        return res


s = 'acdbfdabfr'
p = 'ab'
foo = Solution()
print(foo.findAnagrams(s, p))
