class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        char_pos = {}
        max_length = 1
        left = 0
        #char_positon[s[0]] = 0

        for right in range(len(s)):
            c = s[right]
            if (c in char_pos) and (char_pos[c] >= left):
                left = char_pos[c] + 1
                char_pos[c]=right
            else:
                char_pos[c] = right

            length = right - left + 1
            max_length = max(max_length, length)
        print(char_pos)
        return max_length