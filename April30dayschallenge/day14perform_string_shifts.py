class Solution(object):
    def stringShift(self, s, shift):
        """"
        :type s: string
        :type shift: List[List[int]]
        :rtype: str
        """
        if len(s) < 2:
            return s

        move = sum(sh[1] if sh[0] else -sh[1] for sh in shift) % len(s)
        print(move)

        return s[-move:] + s[:-move]


s = "szugtzxswvztitpnzgtbnusk"
shift = [[1, 18], [1, 18], [1, 5], [1, 18], [0, 3], [0, 13], [1, 23], [0, 4], [0, 22], [0, 15], [0, 3], [0, 16],
         [0, 14], [1, 17], [0, 1], [0, 19], [1, 2], [1, 19], [1, 10], [0, 22], [1, 6], [1, 16], [1, 11], [1, 24]]

foo = Solution()
print(foo.stringShift(s, shift))
