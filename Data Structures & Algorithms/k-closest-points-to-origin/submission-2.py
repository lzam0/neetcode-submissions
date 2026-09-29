class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # iterate through the entire points arr

        arr = []

        for x,y in points:
            dist, coords = x**2 + y**2, [x,y]
            arr.append([dist, coords])

        close = heapq.nsmallest(k, arr)
        
        result = []

        for dist, coord in close:
            result.append(coord)

        print(result)
        # return the closest k coords
        return result