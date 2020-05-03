class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        # myjewels = 0
        #
        # res = set(J).intersection(S) # takes extra memory, not necessary
        #
        # # for j in J:
        # #     if j in S:
        # #         myjewels += S.count(j)
        #
        # for i in res:
        #     myjewels += S.count(i)
        #
        # return myjewels

        return sum(map(J.count, S))  # or binary search: sum(i in J for i in S)


J = "aA"
S = "aAAbbbb"

J = "z"
S = "ZZ"

if __name__ == "__main__":
    foo = Solution()
    print(foo.numJewelsInStones(J, S))

