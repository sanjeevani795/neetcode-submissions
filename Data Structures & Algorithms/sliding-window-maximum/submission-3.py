from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        if k == 1:
            return nums
        
        left = 0
        result = []
        queue = deque()

        for right in range(len(nums)):
            while queue and nums[queue[-1]] <= nums[right]:
                queue.pop()

            queue.append(right)

            if queue and queue[0] < left:
                queue.popleft()

            if right - left + 1 == k:
                result.append(nums[queue[0]])
                left += 1      
            
        return result





        