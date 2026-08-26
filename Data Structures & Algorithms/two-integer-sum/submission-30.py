class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # two soltions pop into my mind
        # firstly we can do a brute force but it would require O(n^2) as it requires a loop within a loop

        # so i think the better approach would be to create an arr 
        # we do target - curr num = value
        # then we find the value
        # if that isnt found then more onto the next index

        arr = {}

        for i in range(len(nums)):
            currNum = nums[i]

            value = target - currNum

            if value in arr:
                return [arr[value], i]
            else:
                arr[currNum] = i

        return []