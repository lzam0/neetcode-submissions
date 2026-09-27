class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        arr = []

        # firstly we can create a max heap
        for stone in stones:
            arr.append(-stone)

        print('before heap',arr)

        # turn maxArr into a heap
        heapq.heapify(arr)

        print('after heap',arr)
        # loop through until the length of arr is larger than 1
        while len(arr) > 1:
            first = heapq.heappop(arr)
            sec = heapq.heappop(arr)

            print('test')
            if first != sec:
                # append the smashed arr into heap
                heapq.heappush(arr, first - sec)

        arr.append(0)
        return abs(arr[0])