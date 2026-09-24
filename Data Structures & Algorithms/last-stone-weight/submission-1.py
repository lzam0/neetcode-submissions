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
            large = -heapq.heappop(new_arr)
            big = -heapq.heappop(new_arr)

            print(large, big)

            # smash the stones together
            new_stone = large - big

            print(new_stone)
            
            # put the remaining stone back into the -ve heap
            heapq.heappush(new_arr, -new_stone)
            
            print(new_arr)
        
        # repeat again
        return -new_arr[0]