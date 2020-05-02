class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = profit = 0
        j = 1
        while (j < len(prices)):
            if (prices[j]- prices[i] > 0):
                profit += (prices[j] - prices[i])
            i += 1
            j += 1

        return profit

        # # minimum price seen so far
        # mini = None
        #
        # max_profit = None
        # buy = None
        # sell = None
        #
        # for index, item in enumerate(prices):
        #
        #     # sell at the minimum - update minimum seen so far
        #     if (mini is None) or (item < mini):
        #         mini = item
        #         buy = index
        #
        #     # buy at the maximum - update maximum seen so far
        #     elif (max_profit is None) or (item - mini) > max_profit:
        #         max_profit = item - mini
        #         sell = index
        #
        # return max_profit

        # minprice = 0
        # maxprofit = 0
        # for i in range(len(prices)):
        #     if prices[i] < minprice:
        #         minprice = prices[i]
        #     elif (prices[i] - minprice) > maxprofit:
        #         maxprofit = prices[i] - minprice
        # return maxprofit
        #

        # # Create profit array and initialize it as 0
        # n = len(prices)
        # profit = [0] * n
        #
        # # Get the maximum profit with only one transaction
        # # allowed. After this loop, profit[i] contains maximum
        # # profit from price[i..n-1] using at most one trans.
        # max_price = prices[n - 1]
        #
        # for i in range(n - 2, 0, -1):
        #
        #     if prices[i] > max_price:
        #         max_price = prices[i]
        #
        #         # we can get profit[i] by taking maximum of:
        #     # a) previous maximum, i.e., profit[i+1]
        #     # b) profit by buying at price[i] and selling at
        #     #    max_price
        #     profit[i] = max(profit[i + 1], max_price - prices[i])
        #
        #     # Get the maximum profit with two transactions allowed
        # # After this loop, profit[n-1] contains the result
        # min_price = prices[0]
        #
        # for i in range(1, n):
        #
        #     if prices[i] < min_price:
        #         min_price = prices[i]
        #
        #         # Maximum profit is maximum of:
        #     # a) previous maximum, i.e., profit[i-1]
        #     # b) (Buy, Sell) at (min_price, A[i]) and add
        #     #    profit of other trans. stored in profit[i]
        #     profit[i] = max(profit[i - 1], profit[i] + (prices[i] - min_price))
        #
        # result = profit[n - 1]
        #
        # return result

def main():
    prices = [7, 6, 4, 3, 1]

    foo = Solution()
    print(foo.maxProfit(prices))


if __name__ == "__main__":
    main()