from _heapq import heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stoneArr = []

        for stone in stones:
            stoneArr.append(-stone)

        print(stoneArr)

        # create a min heap
        heapq.heapify(stoneArr)

        print(stoneArr)

        while len(stoneArr) > 1:
            first = heapq.heappop(stoneArr)
            second = heapq.heappop(stoneArr)

            # check if the stones are not equal to each other
            if first != second:
                heapq.heappush(stoneArr, first - second)
            
            print(stoneArr)
        stoneArr.append(0)

        return abs(stoneArr[0])