class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        # using min heap methodology
        heap = []

        # base it of count dict key
        for num in count.keys():
            # push into heap arr, with count[num] and curr val of num
            heapq.heappush(heap, (count[num], num))

            # if the length of the heap is larger than k
            if len(heap) > k:
                # then pop the smallest element in the arr
                heapq.heappop(heap)

        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res