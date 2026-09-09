class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}

        for i in range(len(nums)):
            # if the currVal is within the count hashmap then end loop and return True (for dup)
            # otherwise add it to the hashmap

            currVal = nums[i]
            if currVal in count:
                return True
            else:
                count[currVal] = 1


        return False