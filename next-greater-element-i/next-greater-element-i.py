class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import defaultdict
        pos = defaultdict(int)
        n1 = len(nums1)
        n2 = len(nums2)
        ans = [-1] * n1
        
        for i, num in enumerate(nums1):
            pos[num] = i
        
        for i in range(n2):
            if nums2[i] not in pos:
                continue
            for j in range(i+1, n2):
                if nums2[j] > nums2[i]:
                    idx = pos[nums2[i]]
                    ans[idx] = nums2[j]
                    break
        return ans