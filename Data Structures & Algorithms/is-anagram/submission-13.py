class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1

        for i in t:
            #if i in count:
            #    count[i] -= 1
            count[i] = count.get(i, 0) - 1

        for d in count.values():
            if d != 0:
                return False

        return True
        

