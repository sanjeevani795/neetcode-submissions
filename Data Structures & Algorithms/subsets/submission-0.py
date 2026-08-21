class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        def helper(i, s, slate, result):
            if i == len(s):
                result.append(slate.copy())
                return

            slate.append(s[i])
            helper(i+1, s, slate, result)
            slate.pop()

            helper(i+1, s, slate, result)

        helper(0, nums, [], result)
        return result
        