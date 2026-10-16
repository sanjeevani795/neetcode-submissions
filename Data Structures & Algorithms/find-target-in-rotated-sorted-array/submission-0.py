class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def targetsearch(low, high):
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid  
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1         

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2
            if nums[high] < nums[mid]:
                low = mid + 1
            else:
                high = mid
        pivot = low
                
        result = targetsearch(0, pivot - 1)
        if result != -1:
            return result
        return targetsearch(pivot, len(nums) - 1)
        