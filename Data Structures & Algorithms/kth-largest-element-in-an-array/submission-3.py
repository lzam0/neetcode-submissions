class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # using the heap n largest function

        return heapq.nlargest(k, nums)[-1]