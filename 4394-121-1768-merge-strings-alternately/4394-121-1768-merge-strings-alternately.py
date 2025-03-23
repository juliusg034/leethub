class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        smallest_len = min(len1, len2)
        ans = []

        # Psuedo Code
        # take first letter of first word
        # take second letter of second word
        # keep alternating
        # if either of them is longer just append the remaining letters

        for i in range(smallest_len):
            ans.append(word1[i])
            ans.append(word2[i])
        
        if len1 > len2:
            num = len1 - len2
            ans.append(word1[-num:])

        if len2 > len1:
            num = len2 - len1
            ans.append(word2[-num:])

        ans = "".join(ans)
        return ans
        