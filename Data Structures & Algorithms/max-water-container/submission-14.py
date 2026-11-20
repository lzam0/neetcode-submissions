class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # INPUT: heights arr
        # OUTPUT: max maxArea

        area = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            b = r - l
            h = min(heights[l], heights[r])
            area = max(area, b*h)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return area