class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        h = len(nums) - 1

        while l < h:
            m = (l + h) // 2
            if nums[m] > nums[h]:
                l = m + 1
            else:
                h = m
        pivot = l

        def targetsearch(l, h):
            while l <= h:
                m = (l + h) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    h = m - 1
            return -1
        
        result = targetsearch(0, pivot - 1)
        if result != -1:
            return result
        
        return targetsearch(pivot, len(nums) - 1)
         
        


        