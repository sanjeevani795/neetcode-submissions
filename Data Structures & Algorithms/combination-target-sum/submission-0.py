class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def helper(i, slate, current_sum):
            if (current_sum == target):
                result.append(slate[:])
                return
            if (i == len(nums) or current_sum > target):
                return
    
            slate.append(nums[i])
            helper(i, slate, current_sum + nums[i])
            slate.pop()

            helper(i+1, slate, current_sum)
        
        helper(0, [], 0)

        return result
        