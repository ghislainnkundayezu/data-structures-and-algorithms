class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] += 1
        
        for e in t:
            count[ord(e) - ord("a")] -= 1
        
        for p in count:
            if p != 0:
                return False

        return True