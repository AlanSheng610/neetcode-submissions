class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        overall = 1
        for i,n in enumerate(nums):
            overall *= n
        
        res = []
        for i, n in enumerate(nums):
            product = 1
            if n == 0:
                for j, k in enumerate(nums):
                    if j != i:
                        product *= k
            else:
                product = int(overall/n)
            
            res.append(product)
        return res
            