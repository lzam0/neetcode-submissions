class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        area = 0

        while l <= r:
            # lets find the width and max heiht we can obtain
            width = r - l
            height = min(heights[l], heights[r])

            area = max(area, (width * height))

            # we move l or r pointer
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return area