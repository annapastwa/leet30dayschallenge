# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, x, y):
#        """
#        :type x : int, y : int
#        :rtype int
#        """
#
#    def dimensions:
#        """
#        :rtype list[]
#        """

class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """

        [nr, nc] = binaryMatrix.dimensions()
        # print('dimensions are: {}, {}'.format(nr, nc))
        r = nr - 1
        c = nc - 1
        left_most = -1

        if nr < 1 or nc < 1:
            return left_most

        while c >= 0:  # loop over columns for most left
            # print(binaryMatrix.get(r, c))
            if binaryMatrix.get(r, c) == 1 and r > 0:
                left_most = c
                c -= 1
                r = nr - 1
            elif binaryMatrix.get(r, c) == 0 and r > 0:
                r -= 1
                if r == 0 and binaryMatrix.get(r, c) == 0:
                    break
                elif r == 0 and binaryMatrix.get(r, c) == 1:
                    left_most = c
                    c -= 1
                    r = nr - 1

        return left_most


matrix1 = [[1, 1, 1, 1, 1],
           [0, 0, 0, 1, 1],
           [0, 0, 1, 1, 1],
           [0, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]]

matrix2 = [[0, 0, 0, 1],
           [0, 0, 1, 1],
           [0, 1, 1, 1]]

# Alternative solution
# class Solution(object):
#     def leftMostColumnWithOne(self, binaryMatrix):
#         """
#         :type binaryMatrix: BinaryMatrix
#         :rtype: int
#         """
#         res, (m, n) = -1, binaryMatrix.dimensions()
#
#         for i in range(m):
#             for j in range(res % n, -1, -1):
#                 if binaryMatrix.get(i, j): res = j
#                 else: break
#
#         return res