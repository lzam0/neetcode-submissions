class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            currSum = numbers[l] + numbers[r]
            if currSum > target:
                # then we must move the right pointer down
                r -= 1
            elif currSum < target:
                # then we must move the left pointer up
                l += 1
            if currSum == target:
                # if we find the target
                return [l+1, r+1]