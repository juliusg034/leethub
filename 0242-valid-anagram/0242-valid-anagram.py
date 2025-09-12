class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}

        for char in s:
            if char in freq1:
                freq1[char] += 1
            else:
                freq1[char] = 1
        
        for char in t:
            if char in freq2:
                freq2[char] += 1
            else:
                freq2[char] = 1
        
        if len(freq1) != len(freq2):
            return False
        
        for key in freq1:
            if key not in freq2:
                return False
            if freq1[key] != freq2[key]:
                return False
        
        return True