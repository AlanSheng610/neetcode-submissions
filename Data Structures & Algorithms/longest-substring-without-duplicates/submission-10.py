class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = {}
        max_window = 0
        while right < len(s):
            if s[right] in seen:
                left = max(left, seen[s[right]] +1)
            seen[s[right]] = right 
            right += 1
            max_window = max (max_window, right - left)
            
            
            # if s[right] not in seen:
            #     seen.add(s[right])
            #     right += 1 
            #     max_window = max(right-left, max_window)
            # else:
            #     seen.remove(s[left])
            #     left += 1
        
        return max_window
        

            
