class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        b = 0

        for e in s:
            if e == '(':
                l += 1
            else:
                l -= 1

            if e != ')':
                b += 1
            else:
                b -= 1
            if b < 0: break

            l = max(l, 0)

        return l == 0


s = "*"
foo = Solution()
print(foo.checkValidString(s))
