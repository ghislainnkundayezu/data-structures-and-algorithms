class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        max_length = 0
        l = 0

        for r in range(len(s)):
            if s[r] in charMap and charMap[s[r]] >= l:
                 
                l = charMap[s[r]] + 1

            charMap[s[r]] = r
            window_length = r - l + 1
            max_length = max(max_length, window_length)
            #else:
            #    charMap[s[r]] = r

        print("$$$")
        print(charMap)
        return max_length