class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        # left pointer -> buying stock
        # right pointer -> selling stock

        # cost = buying stock - selling stock

        bestP = 0

        # loop through the entire arr
            #cost = r - l
            # bestP = max(bestP, cost) - determine which is the best price

        while r < len(prices):
            # if the 10 < 1 which is not we move left pointer to where right pinter is
            if prices[l] < prices[r]:
                cost = prices[r] - prices[l]

                bestP = max(bestP, cost)
            else:
                l = r
            r += 1
        

        return bestP
