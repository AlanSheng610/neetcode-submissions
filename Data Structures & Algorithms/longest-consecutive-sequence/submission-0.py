class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        potential_start = []
        # find start
        for i, n in enumerate(nums):
            if n-1 not in nums_set:
                print(n-1)
                potential_start.append(n)
        # print(potential_start)
        max_count = 0
        for i, n in enumerate(potential_start):
            count = 1
            next = n+1
            while True:
                if next in nums_set:
                    count += 1
                    next += 1
                else:
                    max_count = count if count > max_count else max_count
                    break

        return max_count 