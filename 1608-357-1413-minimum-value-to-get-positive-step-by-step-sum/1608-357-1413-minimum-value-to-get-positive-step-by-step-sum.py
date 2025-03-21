class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        startValue = 1
        n = len(nums)
        prefix = [nums[0]]
        
        # keep running sum by making the new elem the sumation of the last elem and new elem
        for i in range(1,n):
            prefix.append(prefix[-1] + nums[i])
        
        # this will be the lowest the sumation can get in this problem
        minimum = min(prefix)
        
        # if all #s are positive 1 is the smallest startValue
        # otherwise it has to be one int greater than the minimum prefix value -4 + 4 + 1 = 1
        if minimum < startValue:
            return abs(minimum) + 1
        else:
            return startValue
        
            
        
            