class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = float('inf')

        left = 0
        length = 0
        sum = 0
        for right in range(n):
            length += 1
            sum += nums[right]

            if sum == target:
                ans = min(ans, length)           

            while sum > target:
                ans = min(ans, length)
                sum -= nums[left]
                left += 1
                length -= 1

                if sum == target:
                    ans = min(ans, length)
            


        if ans == float('inf'): return 0
        else: return ans
            
