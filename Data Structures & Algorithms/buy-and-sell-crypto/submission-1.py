class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1

        max_profit = 0

        while r < len(prices):
            # check if its profitable
            # if the prices of left is less than right
            if prices[l] < prices[r]:
                # we calculate the current profit
                profit = prices[r] - prices[l]

                # then we check if the curr profit is larger than the max profit
                max_profit = max(max_profit, profit)

            else:

                # dont just shfit by one, shift it all the way to the right bc we found a really low price that we possibly can
                # find the minimum
                l = r


            # repeat right pointer until out of bounds
            r += 1

        return max_profit