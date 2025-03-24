class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        lowercase_ascii = 'abcdefghijklmnopqrstuvwxyz'
        freq = {}
        
        for char in sentence:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
        
        for char in lowercase_ascii:
            if char not in freq:
                return False
            
        return True