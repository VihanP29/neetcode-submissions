class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        l = 0
        r = len(heights) - 1
        while l<r:
            tempArea = min(heights[l],heights[r])*(r-l)
            if tempArea > maxArea:
                maxArea = tempArea
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
            
        return maxArea

        