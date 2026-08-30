class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) -1

        area = 0
        # so we initialise the pointers
        # aftewards we want to shift the pointer values
        
        while l < r:
            # calculate area
            # width * height

            width = r - l
            height = min(heights[l], heights[r])

            # update the highest possible area
            area = max(area, width * height)

            # we save the are to the current values of l and r 
            # move pointer that has the shorter height
            if heights[l] < heights[r]:
                # move left pointer up
                l += 1
            else:
                r -= 1
            
        return area