class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0

        l, r = 0, len(heights) - 1

        for index in heights:
            
            base = r - l
            height = min(heights[l], heights[r])

            area = max(area, base * height)

            # move the pointer
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return area