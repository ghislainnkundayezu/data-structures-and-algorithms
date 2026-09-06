class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        for index, num1 in enumerate(nums):
            for num2 in nums[index+1:]:
                if(num1 == num2):
                    return True

        return False