class Solution:
    def minStartValue(self, nums: List[int]) -> int:

        startValue = 1
        invalid = True
        
        # Keep increasing startValue until its valid
        
        while invalid:
            invalid = False
            runningTotal = startValue
            
            for num in nums:
                runningTotal += num
                if runningTotal < 1:
                    startValue += 1  
                    invalid = True
                    break
            
        return startValue
            