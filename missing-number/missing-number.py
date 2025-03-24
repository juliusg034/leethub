class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            elif num not in freq:
                freq[num] = 1
        
        for num in range(0,n+1):
            if num not in freq:
                return num
            