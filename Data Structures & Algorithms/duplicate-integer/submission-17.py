class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # if value appears more than once in array
        # return false otherwise

        seen = set()

        for val in nums:
            if val in seen:
                return True
            else:
                seen.add(val)

        return False