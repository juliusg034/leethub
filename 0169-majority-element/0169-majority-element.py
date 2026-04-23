class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        most = 0
        ans = 0
        for num in freq:
            if freq[num] > most:
                most = freq[num]
                ans = num
            
        return ans