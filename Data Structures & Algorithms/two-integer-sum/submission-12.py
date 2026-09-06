class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}

        for i in range(len(nums)):
            #if str(nums[i]) not in nums_map:
            nums_map[str(nums[i])] = i
         
        result = []
        for n in range(len(nums)):
            diff = target - nums[n]
             
            if str(diff) in nums_map and nums_map[str(diff)] != n:
                result.extend([n, nums_map[str(diff)]])
                break

        return result
