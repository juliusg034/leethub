class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        ans = []

        for num in nums:
            seen.add(num)

        for i in range(1, len(nums) + 1):
            if i not in seen:
                ans.append(i)

        return ans
        