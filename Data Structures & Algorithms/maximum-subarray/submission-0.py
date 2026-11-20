class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp i = max (nums i , dp i-1 + nums i )

        curMax = nums[0]
        res = nums[0]

        for n in nums[1:]:
            curMax = max(n, curMax+n)
            res = max(res, curMax)
        
        return res