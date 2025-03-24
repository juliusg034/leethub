class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        from collections import defaultdict
        letters = defaultdict(int)
        
        for char in text:
            letters[char] += 1
            
        b = letters["b"] // 1
        a = letters["a"] // 1
        l = letters["l"] // 2
        o = letters["o"] // 2
        n = letters["n"] // 1
        
        return min(b,a,l,o,n)