class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # firstly we create a new arr
        new_arr = []
        
        # since we want to grab the largest stones lets reverse the heap size
        for stone in stones:
            new_arr.append(-stone)
        
        # before heapify
        print(new_arr)

        # turn it into a heap
        # creates a min heap - moving the smallest to the left
        heapq.heapify(new_arr)

        # heapify
        print(new_arr)

        while len(new_arr) > 1:
            # grab the largest stones
            first = heapq.heappop(new_arr)
            second = heapq.heappop(new_arr)

            # lets smash them togehter
            if first != second:
                heapq.heappush(new_arr, first - second)
        
        # if the answer is less than 0 then append 0
        new_arr.append(0)

        print(new_arr)

        return abs(new_arr[0])