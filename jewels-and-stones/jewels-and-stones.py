class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        reference = {}
        freq = {}
        ans = 0

        for j in jewels:
            reference[j] = True
        
        for s in stones:
            if s in reference and reference[s]:
                ans += 1
        
        return ans