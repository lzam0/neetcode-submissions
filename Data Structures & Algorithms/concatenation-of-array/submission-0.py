class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            currVal = nums[i]

            ans.append(currVal)

        return 2*ans