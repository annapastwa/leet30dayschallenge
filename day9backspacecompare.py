class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        s1 = []
        s2 = []

        for e in S:
            if e != "#":
                s1.append(e)
            else:
                if len(s1) > 0:
                    s1.pop()

        for e in T:
            if e != "#":
                s2.append(e)
            else:
                if len(s2) > 0:
                    s2.pop()
        while len(s1) > 0 and len(s2) > 0:
            c1 = s1[-1]
            s1.pop()
            c2 = s2[-1]
            s2.pop()
            if c1 != c2:
                return False

        if len(s1) > 0 or len(s2) > 0:
            return False
        return True


def main():
    S = "acb#c#"
    T = "ad#c"
    foo = Solution()
    print(foo.backspaceCompare(S, T))


if __name__ == "__main__":
    main()
