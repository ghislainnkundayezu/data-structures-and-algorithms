class Solution:

    # def encode(self, strs: List[str]) -> str:
    #     instructions = ""
    #     result = ""
    #     for s in strs:
    #         instructions += (str(len(s))+",")
    #         result += s

    #     instructions += "#"
    #     return instructions + result    

    # def decode(self, s: str) -> List[str]:
    #     instr_index = 0
    #     left = s.find("#") + 1
    #     right = 0
    #     result = []

    #     while s[instr_index] != "#":
    #         s_count = ""
    #         while s[instr_index] != ",":
    #             s_count += s[instr_index]
    #             instr_index += 1

    #         right = left + int(s_count)
    #         result.append(s[left:right])

    #         left = right
    #         instr_index += 1 

    #     return result

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += (str(len(s)) + "#" + s)

        return encoded_string    

    def decode(self, s: str) -> List[str]:
        decoded_substrings = []
        l = r = 0

        while r < len(s):
            length = ""
            while s[l] != "#":
                length += s[l]
                l += 1
        
            l += 1
            r = l + int(length)
            
            decoded_substrings.append(s[l : r])
        
            l = r

        return decoded_substrings