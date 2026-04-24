class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)

        seen = set()
        duplicate = 0

        for num in nums:
            if num in seen:
                duplicate = num
            seen.add(num)

        missing = expected_sum - (actual_sum - duplicate)

        return [duplicate, missing]