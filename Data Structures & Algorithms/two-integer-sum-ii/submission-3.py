class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        # lets move the points from either end and add l + r to check if its equal to target

        while l < r:
            sum = numbers[l] + numbers[r]

            if sum < target:
                l += 1
            elif sum > target:
                r -= 1
            else:
                return [l+1,r+1]
        return []