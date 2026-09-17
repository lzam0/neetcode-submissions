class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}

        for i in range(len(nums)):
            val = nums[i]

            goal = target - val

            if goal in numbers:
                # return the values
                return [numbers[goal], i]
            else:
                # add it to the numbers dict
                numbers[val] = i

        print(numbers)
        return []