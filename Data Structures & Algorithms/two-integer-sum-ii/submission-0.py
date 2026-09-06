class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for ind1, num in enumerate(numbers):
            for ind2, n in enumerate(numbers[ind1+1:], start = (ind1+1)):
                if num + n == target:
                    return [ind1+1, ind2+1]