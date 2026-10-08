class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        
        l = 0
        r = len(heights) - 1
    
        while l < r:
            # get width
            width = r - l

            # get height
            height = min(heights[l], heights[r])
            
            # max area
            area = max(area, width * height)

            # we determine the move of the pointer whether L OR R pointer is larger
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return area