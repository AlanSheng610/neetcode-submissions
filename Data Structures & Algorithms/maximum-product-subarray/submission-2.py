class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = nums[0]
        curMin = nums[0]
        res = nums[0]

        for n in nums[1:]:
            newMax = max(n, n * curMax, n * curMin)
            newMin = min(n, n * curMax, n * curMin)
            curMax = newMax
            curMin = newMin
            res = max(curMax, res) 
        
        return res