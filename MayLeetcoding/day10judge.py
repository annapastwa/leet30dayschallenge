import collections


class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
# My suboptimal solution that works
        # if N == 2 and len(trust) == 1:
        #     return trust[0][1]
        #
        # firsts = collections.Counter([x[0] for x in trust])
        # seconds = collections.Counter([x[1] for x in trust])
        # # print(firsts, firsts.keys(), sum(firsts.keys()), seconds)
        # judge = sum(set(range(1, N + 1))) - sum(firsts.keys())
        #
        # if len(firsts.keys()) == N - 1 and seconds[
        #     judge] == N - 1 and judge not in firsts.keys():  # trusts noone so neve 1st
        #     return judge
        # return -1

        # Better solution of graph properties
        #Keep track of the cumulative score of each person: if person a trusts person b, we decrement a's score and increment b's score.
        count = [0] * (N + 1)
        print(count)
        for i, j in trust:
            print(i,j)
            count[i] -= 1
            count[j] += 1
        print(count)
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1

N = 4
#trust = [[1, 3], [2, 3]]
#  [[1, 2]]
trust = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]

foo = Solution()
print(foo.findJudge(N, trust))
