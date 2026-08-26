class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # key: amount
        arr = {}

        for i in range(len(nums)):
            curr = nums[i]

            if curr not in arr:
                arr[curr] = 1
            else:
                return True
            
        return False