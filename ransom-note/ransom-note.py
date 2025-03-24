class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import defaultdict
        freq = defaultdict(int)
        
        for char in magazine:
            freq[char] +=1
            
        for char in ransomNote:
            freq[char] -= 1
            if freq[char] == -1:
                return False
        
        return True