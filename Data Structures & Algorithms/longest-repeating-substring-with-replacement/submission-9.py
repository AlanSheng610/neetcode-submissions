class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        seen = {}
        max_count = 0
        count = 0
        for r, char in enumerate(s):
            # r == l > r move
            # r != l
            #  1. count < k => r move and count ++
            #  2. count >= k  => l move 

            # window size - max freq <= k
            seen[char] = seen.get(char,0) + 1
            max_freq = max(seen.values())

            while (r - l + 1) - max_freq > k:
                seen[s[l]] -= 1
                l += 1
                max_freq = max(seen.values())
                
            
            max_count = max(max_count, r-l+1)

        return max_count 

