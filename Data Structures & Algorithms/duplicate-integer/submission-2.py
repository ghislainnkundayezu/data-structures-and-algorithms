class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # create a count map
        count = set()
        for i in range(len(nums)):
            if nums[i] in count:
                return True
            count.add(nums[i])
            
        return False

