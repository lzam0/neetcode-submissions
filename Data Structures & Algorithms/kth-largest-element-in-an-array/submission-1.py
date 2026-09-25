class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # firstly we can make the arr into a max heapify
        maxHeap = []

        for num in nums:
            maxHeap.append(-num)

        heapq.heapify(maxHeap)

        val = 0
        for i in range(k):
            val = heapq.heappop(maxHeap)

        return -val