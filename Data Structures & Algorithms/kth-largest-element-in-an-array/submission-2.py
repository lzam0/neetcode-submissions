class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # firstly we can make the arr into a max heapify
        maxHeap = []
        
        # reverse nums
        for num in nums:
            maxHeap.append(-num)

        # create a min heap of the largest values
        heapq.heapify(maxHeap)

        val = 0
        # get the Kth index value of the arr
        for i in range(k):
            val = heapq.heappop(maxHeap)

        return -val