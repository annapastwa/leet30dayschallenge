# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        Solve with binary search to minimize the number of API calls
        We use three pointers: low end, mid for the API call and high end
        In linear search the time complexity would be O(n)
        :type n: int
        :rtype: int
        """
        low = 1
        high = n

        while low < high:
            mid = (low + high) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low


def isBadVersion(i):
    versions = [False, False, False, False, True]
    return versions[i-1]


foo = Solution()
print(foo.firstBadVersion(5))
