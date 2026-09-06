class Solution:

    def encode(self, strs: List[str]) -> str:
        instructions = ""
        result = ""
        for s in strs:
            instructions += (str(len(s))+",")
            result += s

        instructions += "#"
        return instructions + result    

    def decode(self, s: str) -> List[str]:
        instr_index = 0
        left = s.find("#") + 1
        right = 0
        result = []

        while s[instr_index] != "#":
            s_count = ""
            while s[instr_index] != ",":
                s_count += s[instr_index]
                instr_index += 1

            right = left + int(s_count)
            result.append(s[left:right])

            left = right
            instr_index += 1 

        return result
