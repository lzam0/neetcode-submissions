class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # variable to update when theres a better profit margin
        bestROI = 0
        
        # sets the min price to the first object in the arr
        minPrice = prices[0]
        
        for i in range(len(prices)):
            # find the lowest price we have currently
            minPrice = min(prices[i], minPrice)

            # curr profit = sell price - buy price
            profit = prices[i] - minPrice

            # best margin = select between the higher value of the bestROI var and curr profit
            bestROI = max(bestROI, profit)

        return bestROI