class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        a_idx = 0
        b_idx = 0
        output = []

        while a_idx < len(A) and b_idx < len(B):
            start = max(A[a_idx][0], B[b_idx][0])  # take bigger value for intersection start
            end = min(A[a_idx][1], B[b_idx][1])  # take smaller value for intersection end
            if start <= end:
                output.append([start, end])
            if A[a_idx][1] < B[b_idx][1]:
                a_idx += 1
            else:
                b_idx += 1

        return output


A = [[0, 2], [5, 10], [13, 23], [24, 25]]
B = [[1, 5], [8, 12], [15, 24], [25, 26]]

foo = Solution()
print(foo.intervalIntersection(A, B))
