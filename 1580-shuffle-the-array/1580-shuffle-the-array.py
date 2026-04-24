class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        length = n * 2
        ans = []

        left = 0
        right = n

        while right < length:
            ans.append(nums[left])
            ans.append(nums[right])

            right += 1
            left += 1
        
        return ans
