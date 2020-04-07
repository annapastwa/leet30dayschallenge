# Given an integer array arr, count element x such that x + 1 is also in arr.
# If there're duplicates in arr, count them seperately.

class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        c = 0
        sarr = list(set(arr))

        d = {x: arr.count(x) for x in arr}
        # print(d, len(d))

        if len(sarr) < 2:
            return c
        for i in range(len(sarr)-1):
            if sarr[i+1] == sarr[i]+1:

                c += d[sarr[i]] # number of times left appears

        # for i in range(len(arr)):
        #     for j in range(len(arr)):
        #         if arr[j]==arr[i]+1:
        #             c += 1
        #             break

        return c





def main():
    arr = [1,1,2]

    foo = Solution()
    print(foo.countElements(arr))


if __name__ == "__main__":
    main()