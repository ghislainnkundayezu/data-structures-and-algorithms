class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs: 
            res += f"{len(word)}#{word}"
        return res

    def decode(self, s: str) -> List[str]:
        c = 0
        res = []
        while c < len(s):
            count = ""
            while s[c].isdigit():
                count += s[c]
                c += 1
            res.append(s[c + 1 : c + int(count) + 1])
            c = c + int(count) + 1
        return res