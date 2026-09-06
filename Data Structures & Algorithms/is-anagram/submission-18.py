class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charMap = {}
        for c in s:
            charMap[c] = charMap.get(c, 0) + 1
        
        for e in t:
            if e not in charMap:
                return False
            charMap[e] -= 1
        
        for g in charMap:
            if charMap[g] != 0:
                return False

        return True