class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0

        while l < r:
            width = r - l
            height = min(heights[l], heights[r])
            # what ever is the shorter height we move
            if heights[l] <  heights[r]:
                l += 1
            else:
                r -= 1
            area = max(area, height*width)
        return area