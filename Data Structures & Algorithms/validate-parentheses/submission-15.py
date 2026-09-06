class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {
            "{": "}",
            "[": "]",
            "(": ")"
        }

        line = []

        for char in s:
            if char in char_map:
                line.append(char)
            elif line and char_map[line[-1]] == char:
                line.pop()
                
            else:
                return False

        if len(line) != 0: return False

        return True