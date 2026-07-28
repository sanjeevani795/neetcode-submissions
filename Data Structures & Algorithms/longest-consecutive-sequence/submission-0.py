class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_hash = set(nums)
        count = 0
        for num in nums:
            if num-1 not in nums_hash:
                length = 0
                curr = num
                while curr in nums_hash:
                    length += 1
                    curr += 1
                count = max(count, length)

        return count

        