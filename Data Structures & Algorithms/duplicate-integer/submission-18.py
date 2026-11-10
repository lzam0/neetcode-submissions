class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # has a duplicate = true
        # no duplicate = false

        # hash sets
        count = set()

        for val in nums:
            if val in count:
                return True
            else:
                count.add(val)

        return False