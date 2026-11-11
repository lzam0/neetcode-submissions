class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # reutnr i and j so that nums[i] + nums[j] = target
        # i != j
        

        # plan:
        # we can do a brute force approach
        # where i can loop through i + j until target is found

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i,j]

        return []