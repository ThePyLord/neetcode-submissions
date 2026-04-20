class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s = 0
        f = len(heights) - 1
        best_container = -math.inf
        while s <= f:
            w = f - s # Width
            # Height (use minimum value since water overflows the lower height)
            h = min(heights[s], heights[f]) 
            area = w * h
            
            if heights[s] < heights[f]:
                s += 1
            else:
                f -= 1

            best_container = max(best_container, area)
        
        return best_container