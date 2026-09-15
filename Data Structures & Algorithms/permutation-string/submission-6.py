class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1 = "".join(sorted(s1))
        l, r = 0, len(s1)-1

        while r < len(s2):
            sub = "".join(sorted(s2[l : r + 1]))
            print(sub)
            if sub == s1:
                return True
            
            l += 1
            r += 1

        return False