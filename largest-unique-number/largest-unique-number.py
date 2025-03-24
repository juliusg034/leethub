class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        from collections import defaultdict
        freq = defaultdict(int)
        
        ans = -1
        
        for key in nums:
            freq[key] += 1
            
        for key in freq:
            if freq[key] == 1:
                ans = max(ans, key)
                
        return ans