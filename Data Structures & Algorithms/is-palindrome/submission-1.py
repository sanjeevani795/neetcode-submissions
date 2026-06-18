class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = s.replace(" ", "").lower()
        clean_s = re.sub(r'[^a-zA-Z0-9]', '', new_s)

        first = 0
        last = len(clean_s) - 1

        while (first < last):
            if clean_s[first] != clean_s[last]:
                return False
            first += 1
            last -= 1
        
        return True