class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [0] * 2
        check = set()

        for num in nums:
            if num not in check:
                check.add(num)
            else:
                ans[0] = num

        for i in range(1,len(nums)+1):
            if i not in check:
                ans[1] = i
                break

        return ans