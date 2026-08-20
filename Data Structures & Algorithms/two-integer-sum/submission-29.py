class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # value: index
        vals = {}
        for i in range(len(nums)):
            value = nums[i]
            print(nums[i])

            find = target - value

            if find in vals:
                return [vals[find], i]

            vals[value] = i
            
            

        return []