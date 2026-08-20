class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        arr = {}

        for i in range(len(nums)):
            curr = nums[i]

            if curr in arr:
                # curr val already in arr
                return True
            else:
                # not in dict
                arr[curr] = 1


        return False