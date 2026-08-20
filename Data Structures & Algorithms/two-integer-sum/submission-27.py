class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}

        #  loop through the array
        for i in range(len(nums)):
            # get the difference 
            diff = target - nums[i]

            # check if the difference is inside of the vals dict
            if diff in vals:
                print("Difference is inside of the dict")
                return [vals[diff], i]
            
            vals[nums[i]] = i

        return []