class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+" : lambda x, y : x + y,
            "-" : lambda x, y : x - y, 
            "*" : lambda x, y : x * y,
            "/" : lambda x, y : int(float(x) / y)
        }

        operands = []

        for token in tokens:
            if token in operations:
                y, x = operands.pop(), operands.pop()
                ans = operations[token](x, y)
                operands.append(ans)
            else:
                operands.append(int(token))

         
        return operands[0]



