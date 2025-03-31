class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        p1 = 0
        p2 = 0
        common = -1
        
        while p1 < len(nums1) and p2 < len(nums2):
            num1 = nums1[p1]
            num2 = nums2[p2]
            
            if num1 == num2:
                return num1
            
            if num1 > num2:
                p2 += 1
            else:
                p1 += 1
            
        return common