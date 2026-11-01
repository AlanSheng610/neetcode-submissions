class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 1
        window = 1
        seen = set()
        if s =="":
            return 0
        seen.add(s[left])
        max_window = 1
        while right < len(s):
            
            if s[right] not in seen:
                seen.add(s[right])
                right += 1 
                window += 1
                max_window = max(window, max_window)
            else:
                seen.remove(s[left])
                left += 1
                window -= 1
        
        return max_window
        

            
