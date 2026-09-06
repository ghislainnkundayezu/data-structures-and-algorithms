class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)

        for i, e in enumerate(temperatures):
            while stack and stack[-1][1] < e:
                index, element = stack[-1][0], stack[-1][1]
                result[index] = i - index

                stack.pop()

            stack.append((i, e))

        return result