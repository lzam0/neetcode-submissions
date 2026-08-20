class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # firstly we find the middle value
        # then afterwards we can check if middle value is > or < than target
        length = len(nums)
        middle = (length / 2) + 1

        # brute force approach
        for i in range(length):
            curr = nums[i]
            print(i)

            if curr == target:
                return i
        
        return -1