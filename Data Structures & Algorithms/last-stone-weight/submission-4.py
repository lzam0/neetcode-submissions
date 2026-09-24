class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        new_arr = []
        
        # turn the stone arr into -ve
        for stone in stones:
            new_arr.append(-stone)

        print(new_arr)

        # turn the new arr into a heap
        heapq.heapify(new_arr)

        # heap new arr
        print(new_arr)
        
        while len(new_arr) > 1:
            # obtain the 'largest' ones
            first = heapq.heappop(new_arr)
            second = heapq.heappop(new_arr)


            # check if the two stones can be smashed
            if first != second:
                # smash together
                heapq.heappush(new_arr, first - second)
        
        # repeat again
        new_arr.append(0)
        return -new_arr[0]