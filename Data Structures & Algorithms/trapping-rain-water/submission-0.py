class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        maxl = 0
        maxr = len(height) - 1
        left = 0
        right = len(height) - 1
        result = 0

        while left < right:
            if height[maxl] < height[maxr]:
                left += 1
                if height[maxl] < height[left]:
                    maxl = left
                result += height[maxl] - height[left]
            else:
                right -= 1
                if height[maxr] < height[right]:
                    maxr = right
                result += height[maxr] - height[right]
        return result
