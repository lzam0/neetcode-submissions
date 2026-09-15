class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we always need to repeatively remove the two heaviest stones

        # max heap approach is effective to extract the largest rocks

        # convert stones to negative to build a heap
        stones = [-s for s in stones]
        heapq.heapify(stones)

        # while the length of stones is greater than 1 then
        while len(stones) > 1:
            # find the first stone
            first = heapq.heappop(stones)

            # find the second stone
            second = heapq.heappop(stones)

            if first < second:
                heapq.heappush(stones, first - second)

            pass
        stones.append(0)
        return abs(stones[0])