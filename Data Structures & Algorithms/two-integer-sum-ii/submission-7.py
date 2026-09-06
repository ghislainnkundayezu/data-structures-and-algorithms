class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        while r > l:
            sum_ = nums[r] + nums[l]
            if sum_ < target:
                l += 1
            elif sum_ > target:
                r -= 1
            else:
                return [l+1, r+1]
