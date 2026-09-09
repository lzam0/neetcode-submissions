class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}

        # HASHMAP VALUE value: position
        
        # loop through the arr
        # check if curr val is in the hashmap, 
        # if its not then we add it into the hashmap
        # based on its position within the nums arr

        # then we also find target with 2 int values within the arr
        # goal = target - currVal
        # then we find if the goal is within the hashmap and find the position of it


        for i in range(len(nums)):
            currVal = nums[i]
            goal = target - currVal
            if goal in arr:
                return [arr[goal], i]

            # add it into the hashmap
            arr[currVal] = i
        return [] 