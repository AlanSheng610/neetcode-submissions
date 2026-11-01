class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. 統計每個數字的出現次數
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # 2. 建立桶：索引代表出現次數
        bucket = [[] for _ in range(len(nums) + 1)]

        # 3. 將數字放進對應的桶
        for num, freq in count.items():
            bucket[freq].append(num)

        # 4. 從最高頻率往下，收集 k 個數字
        result = []

        for freq in range(len(nums), 0, -1):
            for num in bucket[freq]:
                result.append(num)

                if len(result) == k:
                    return result

        return result

        