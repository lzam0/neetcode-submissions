class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # value: index

        arr = {}

        for i in range(len(nums)):
            currNum = nums[i]

            if currNum not in arr:
                print(currNum)
                arr[currNum] = 1
            else:
                return True
            
        return False