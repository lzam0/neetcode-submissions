class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0

        for r in range(len(nums)):
            # check if our window is too large
            if r - l > k:
                # remove the left most value
                window.remove(nums[l])
                l += 1

            # check if the value is within the set first
            if nums[r] in window:
                # found a duplicate
                return True
            window.add(nums[r])
            # if it isnt then add it to the set

        return False