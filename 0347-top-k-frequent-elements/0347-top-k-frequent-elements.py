class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            
        first_k_keys = list(sorted(count.keys(), key=count.get, reverse=True))[:k]
        return first_k_keys