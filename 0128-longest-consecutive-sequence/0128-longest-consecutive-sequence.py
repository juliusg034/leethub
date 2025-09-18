class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        length = 0
        maximum = 0
        for key in freq:
            if key-1 in freq:
                continue
            while key in freq:
                length += 1
                maximum = max(maximum, length)
                key += 1
            length = 0

        return maximum