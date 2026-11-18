class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            print(nums[mid])
            
            # binary search:
            # l + r // 2
            # check if mid is target
            # if mid not target
            # -> check if its greater or smaller
            # SMALLER -> discard all of the values on the left and assign the new l to mid
            # GREATER -> discard all values on the right and assign new r to mid

            if nums[mid] == target:
                return mid

            # move pointer if its less than target
            if nums[mid] < target:
                l = mid + 1
            else:
                # move pointer if more than target
                r = mid - 1

        return -1