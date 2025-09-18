class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(dict.fromkeys(nums))
        nums.sort()

        res = []
        maxLength = 0
        currLength = 0

        for i, num in enumerate(nums):
            # is the current num the previous nums + 1
            if i == 0:
                currLength = 1
                maxLength = 1
                continue
            if nums[i-1] == num - 1:
                currLength += 1
                maxLength = max(maxLength, currLength)
            else:
                currLength = 1
            

        
        return maxLength