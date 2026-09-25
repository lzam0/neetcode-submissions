class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # k indiciating the amount of shortest value wanted to be returned

        distArr = []

        # grab the points
        for x,y in points:
            # print(x,y)
            
            # we calculate euclidean distance
            #  sqrt((x new distance - x origin)^2 + (y new distance - y origin)^2)
            dist = x**2 + y**2
            distArr.append([dist, [x,y]])

        print(distArr)

        # create a heap
        heapq.heapify(distArr)

        print(distArr)
        kDist = []

        # would grab the smallest distance so its a min heap
        # loop through the heap to return the k amount of elements in the arr
        for i in range(k):
            dist, points = heapq.heappop(distArr)
            print(dist, points)
            kDist.append(points)
            # then we would append to our new arr
        
        print(kDist)
        return kDist