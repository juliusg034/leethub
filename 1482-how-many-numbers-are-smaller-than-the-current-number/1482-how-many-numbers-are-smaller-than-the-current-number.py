class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = {}
        ans = []

        for i, num in enumerate(sorted(nums)):
            if num not in counts:
                counts[num] = i
        
        for num in nums:
            ans.append(counts[num])

        return ans
