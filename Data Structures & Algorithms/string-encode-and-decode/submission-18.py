class Solution:

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for w in strs:
            enc += f"{len(w)}#{w}"
        return enc

    def decode(self, s: str) -> List[str]:
        dec = []
        currentIndex = 0

        while currentIndex < len(s):
            pos = currentIndex
            length = 0

            while s[pos] != "#":
                length = (length * 10) + int(s[pos])
                pos += 1
            
            start, end = pos + 1, pos + 1 + length
            
            dec.append(s[start:end])
            currentIndex += (end - currentIndex)
        
        return dec


