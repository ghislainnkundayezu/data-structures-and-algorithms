class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {
            "{" : "}",
            "[" : "]",
            "(" : ")"
        }
        stack = []
        print(s)
        for e in s:
            if e in char_map:
                stack.append(e)
            
            elif not stack:
                return False
            
            else:
                last = stack.pop()
                if char_map[last] != e:
                    return False
        return len(stack) == 0