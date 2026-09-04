class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0

        for r in range(len(nums)):
            # if the current value doesnt equal to target value
            if nums[r] != val:
                # replace the current index value of the left pointer to value of right pointer
                nums[l] = nums[r]
                
                # increment l
                l +=1
        
        return l