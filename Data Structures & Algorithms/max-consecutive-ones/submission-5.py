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
                if counter > maxCounter:
                    maxCounter = counter
            else:
                # if not a 1
                counter = 0

            

        return maxCounter