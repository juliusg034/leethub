class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        most = 0
        curr = 0

        for num in nums:
            if num == 0:
                curr = 0
            else:
                curr += 1
                most = max(most, curr)
        return most