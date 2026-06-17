from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        freq_s = Counter(s)
        freq_t = Counter(t)

        for char, freq in freq_s.items():
            if char not in freq_t:
                return False
            elif freq != freq_t[char]:
                return False
        return True
                
