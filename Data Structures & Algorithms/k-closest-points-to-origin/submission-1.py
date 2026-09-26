class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        coord = []

        for x,y in points:
            dist = math.sqrt(x**2 + y**2)
            coord.append([dist, [x, y]])

        heapq.heapify(coord)

        ans = []

        for i in range(k):
            dist, points = heapq.heappop(coord)
            ans.append(points)
        # return the closest point
        return ans