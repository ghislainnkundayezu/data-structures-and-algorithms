class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSubString = 0
        seen = {}

        l = 0

        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= l:
                l = seen[s[i]] + 1
                #seen[s[i]] = i
            
            seen[s[i]] = i
            maxSubString = max(maxSubString, i - l + 1)
        
        return maxSubString