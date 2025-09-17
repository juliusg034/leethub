class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter

        count = Counter(nums)

        return heapq.nlargest(k, count.keys(), key=count.get)



