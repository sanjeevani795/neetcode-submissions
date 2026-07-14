from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = Counter(s1)

        k = len(s1)
        left = 0

        for right in range(k-1, len(s2)):
            if right - left + 1 != k:
                left += 1

            freq = Counter(s2[left:right+1])

            if freq == freq_s1:
                return True
        
        return False