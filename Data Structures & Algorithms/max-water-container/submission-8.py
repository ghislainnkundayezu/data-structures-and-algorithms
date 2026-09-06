class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights) - 1
        max_area = float('-inf')
        l, r = 0, n

        while l < r:
            print(l, r)
            h = min(heights[l], heights[r])
            #print(h)
            w = r - l
            area = h * w
             
            max_area = max(max_area, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1 

        return max_area