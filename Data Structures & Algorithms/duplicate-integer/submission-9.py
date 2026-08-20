class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # hashset solution

        # create a seen hashset
        seen = set()

        # loop through the arr
        for num in nums:
            # if num is inside of seen set
            if num in seen:
                return True

            # otherwise add it to the hashset
            seen.add(num)

        # return false if no dups
        return False