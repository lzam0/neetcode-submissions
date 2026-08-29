class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # can use a hashset approach
        # bare in mind that sets are NOT organised so we sort them

        result = set()
        nums.sort()

        for i in range(len(nums)):
            seen = set()

            for j in range(i + 1, len(nums)):
                # find the THIRD element
                # nums[i] + nums[j] + third = 0
                third = -(nums[i] + nums[j])


                # find third element within the hashset
                if third in seen:
                    # then add it to result set
                    result.add((nums[i], nums[j], third))

                # add the curr value into seen set - regardless
                seen.add(nums[j])

        return [list(t) for t in result]