class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:

            if num-1 in numset:
                continue
            
            curr_length = 0
            while num in numset:
                curr_length += 1
                longest = max(longest, curr_length)
                num += 1

        return longest
