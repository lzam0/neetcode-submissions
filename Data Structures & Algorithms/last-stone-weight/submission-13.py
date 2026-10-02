class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stoneArr = []

        for stone in stones:
            stoneArr.append(-stone)

        heapq.heapify(stoneArr)

        while len(stoneArr) > 1:
            # grab the 2 largest stones
            first = heapq.heappop(stoneArr)
            second = heapq.heappop(stoneArr)

            print(first, second)

            # smash stones together
            if first != second:
                heapq.heappush(stoneArr, first - second)

            print(stoneArr)
        
        stoneArr.append(0)

        return abs(stoneArr[0])