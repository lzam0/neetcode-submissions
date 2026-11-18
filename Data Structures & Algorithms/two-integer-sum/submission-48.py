class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # VALUE : KEY
        # NUMBER: INDEX
        values = {}
        
        # iterate through the entire arr ***
        # print indexes ***
        # print numbers of the arr ***

        # find the difference -> diff = target - nums[index] ***
        # check if diff is inside of the values hashmap ***
        # return the values of index and the diff

        # OTHERWISE if it isnt inside of the hashmap then we add it to the hashmap values
        # values[nums[index]] = index

        # OUTSIDE OF FOR LOOP
        # return []

        for index in range(len(nums)):
            # print(nums[index], index)

            diff = target - nums[index]

            if diff in values:
                 return [values[diff], index]

            values[nums[index]] = index

        return []