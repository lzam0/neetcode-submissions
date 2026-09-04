class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxCounter = 0
        for i in range(len(nums)):
            # check if currVal is a 1
            currVal = nums[i]
            if currVal == 1:
                # increment it
                counter += 1
            else:
                print('counter val', counter)
                if counter > maxCounter:
                    maxCounter = counter
                # reset the counter
                counter = 0
        if counter > maxCounter:
            maxCounter = counter
        return maxCounter