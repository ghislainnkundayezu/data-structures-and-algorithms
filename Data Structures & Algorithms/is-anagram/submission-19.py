class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        charMap = {}
        for i in range(len(s)):
            charMap[s[i]] = charMap.get(s[i], 0) + 1
            charMap[t[i]] = charMap.get(t[i], 0) - 1
        
        for g in charMap:
            if charMap[g] != 0:
                return False

        return True