class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = set()
        max_window = 0
        while right < len(s):
            
            if s[right] not in seen:
                seen.add(s[right])
                right += 1 
                max_window = max(right-left, max_window)
            else:
                seen.remove(s[left])
                left += 1
        
        return max_window
        

            
