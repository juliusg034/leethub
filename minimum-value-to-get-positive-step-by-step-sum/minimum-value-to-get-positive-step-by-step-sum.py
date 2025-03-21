class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 1
        n = len(nums)
        prefix = [nums[0]]
        
        for i in range(1,n):
            prefix.append(prefix[-1] + nums[i])
            
        minimum = min(prefix)
        
        if minimum < startValue:
            return abs(minimum) + 1
        else:
            return startValue
        
            
        
            