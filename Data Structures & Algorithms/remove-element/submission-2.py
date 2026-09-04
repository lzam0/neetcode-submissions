class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            # if the value INVALID
            if nums[l] == val:
                # move right pointer closer
                r -= 1

                # replace nums[l] with right pointer value
                nums[l] = nums[r]
            else:
                # if the value is valid
                # increment the left pointer
                l += 1


        return l