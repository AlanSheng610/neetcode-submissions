class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # area=  min(height[i],height[j]) *i-j
        left = 0
        right = len(heights) - 1
        max_area = 0
        while left < right:
            cur_area = min(heights[left],heights[right]) * (right - left)
            max_area = cur_area if cur_area > max_area else max_area

            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_area
            