class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def fun(prev_sum, i):

            if prev_sum == target:
                res.append(path.copy())
                return
            
            if prev_sum > target or i >= len(nums):
                return 
            path.append(nums[i])
            fun(prev_sum + nums[i], i)
            path.pop()

            
            fun(prev_sum , i + 1)
        fun(0,0)
        return res
