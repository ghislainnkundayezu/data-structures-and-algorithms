class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count = {}
        for n in range(len(s)):
            if s[n] not in char_count:
                char_count[s[n]] = 1
            else:
                char_count[s[n]] += 1
        print(char_count)
        for c in t:
            if c in char_count:
                char_count[c] -= 1
             
        print(char_count)    
        for count in char_count.values():
            if count != 0:
                return False
        return True
        
        # return sorted(s) == sorted(t)