class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        left = ans = 0
        
        for right in range(len(s)):
            if s[right] not in freq:
                freq[s[right]] = 1
            else:
                freq[s[right]] += 1
                
            
            while freq[s[right]] > 1:
                freq[s[left]] -= 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans
            