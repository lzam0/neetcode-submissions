class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            # check if left is smaller than right (buying + selling signals)

            if prices[l] < prices[r]:
                # calculate the current profit (buying price - selling price)
                profit = prices[r] - prices[l]

                # determins which is the best selling point
                maxP = max(maxP, profit)

            else:
                # find the min buying value
                l = r

            # increment the buying pointer
            r += 1

        return maxP