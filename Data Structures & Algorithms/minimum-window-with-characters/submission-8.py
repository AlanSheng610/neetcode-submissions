class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        min_len = float("inf")
        min_substring = ""
        need = {}
        # hash table record s freq O(n)
        for r, char in enumerate(t):
            need[char] = need.get(char,0) + 1

        window = {}
        required = len(need)
        formed = 0
        l = 0
        for r, char in enumerate(s):
            window[char] = window.get(char,0) + 1
            # print(formed)
            if char in need and window[char] == need[char]:
                formed += 1

            while formed == required:
                if r - l + 1 < min_len:
                    min_substring = s[l:r+1]
                    min_len = r - l + 1

                # print(r,l)
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1

        return min_substring

                
