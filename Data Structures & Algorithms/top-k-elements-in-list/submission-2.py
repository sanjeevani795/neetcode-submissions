import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []
        hash_nums = Counter(nums)

        for num, value in hash_nums.items():
            heapq.heappush(min_heap, (value, num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        result = [num for value, num in min_heap]

        return result