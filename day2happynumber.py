# Determine if a number is "happy"
# Starting with any positive integer, replace the number by the sum of the squares of its digits,
# and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy numbers.
# The unhappy number will result in a cycle of 4, 16, 37, 58, 89, 145, 42, 20, 4, ....

class Solution(object):
    def isHappy(selfself, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False

        def div_sum(n):
            sum = 0
            while n > 0:
                sum += (n % 10) ** 2
                n = n // 10
            return sum

        result = div_sum(n)
        while result != 1 or result !=4:
            result = div_sum(result)
            if result == 1:
                return True
            if result == 4:
                return False


def main():
    n = 1
    foo = Solution()
    print(foo.isHappy(n))


if __name__ == '__main__':
    main()
