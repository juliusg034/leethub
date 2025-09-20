class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}

        left, right = 0, 0
        longest = 0

        while right < len(s):
            if s[right] not in freq or freq[s[right]] == 0:
                freq[s[right]] = 1
                longest = max(longest, (right - left + 1))
                right += 1
            elif s[right] in freq:
                freq[s[right]] += 1
                while freq[s[right]] > 1:
                    freq[s[left]] -= 1
                    left += 1
                right += 1

        return longest