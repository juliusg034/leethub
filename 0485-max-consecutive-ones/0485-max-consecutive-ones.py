class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        stack = []
        most = 0
        curr = 0

        for num in nums:
            if num == 0:
                stack.clear()
                continue
            
            stack.append(num)
            curr = len(stack)
            most = max(most, curr)

        return most