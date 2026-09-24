from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        if len(s) < len(t):
            return ""
        
        left = 0
        result = ""
        result_length = float('inf')
        map_t = Counter(t)
        map_window = {}
        need = len(map_t)
        have = 0

        for right in range(len(s)):
            if s[right] in map_t:
                map_window[s[right]] = map_window.get(s[right], 0) + 1
                if map_window[s[right]] == map_t[s[right]]:
                    have += 1
                have == need


            while have == need:
                window_len = right - left + 1
                if window_len < result_length:
                    result_length = window_len
                    result = s[left:right + 1] 
                if s[left] in map_t:
                    if map_window[s[left]] == map_t[s[left]]:
                        have -= 1

                    map_window[s[left]] -= 1
                left += 1
            
        return result      
            
            

        



            

            
            
            
