class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        freq = {}
        
        for char in sentence:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
                
            if len(freq) == 26:
                return True
        
        return False