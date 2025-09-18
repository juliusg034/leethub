class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefix = []
        suffix = []

        product = 1
        for num in nums:
            product *= num
            prefix.append(product)

        product = 1
        for num in reversed(nums):
            product *= num
            suffix.append(product)

        suffix.reverse()

        for i, num in enumerate(nums):
            if i == 0:
                res.append(suffix[i+1])
            elif i == len(nums) - 1:
                res.append(prefix[i-1])
            else:
                res.append(prefix[i-1]*suffix[i+1])

        return res