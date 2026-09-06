class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        for e in t:
            if e not in count:
                return False
            count[e] = count.get(e) - 1
                

        for i in count:
            if count[i] != 0:
                return False

        return True