class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals = {}

        # essentially,
        #  we ONLY append it if the difference isnt inside of the vals dict

        #  loop through the array
        for i in range(len(nums)):
            # get the difference 
            diff = target - nums[i]

            # check if the difference is inside of the vals dict
            if diff in vals:
                print("Difference is inside of the dict")
                return [vals[diff], i]
            
            # append ONLY if 
            vals[nums[i]] = i

        return []