class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for w in strs:
            enc += (str(len(w)) + "#") + w
        return enc

    def decode(self, s: str) -> List[str]:
        dec = []
        l = 0 
        r = 0

        while l < len(s):
            word_len = ""
            while s[l] != "#":
                word_len += s[l]
                l += 1
            
            size = int(word_len)
            l += 1
            r = l + size 
            dec.append(s[l:r])
            l = r
            
        return dec
