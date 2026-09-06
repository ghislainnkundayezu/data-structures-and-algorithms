class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        threshhold = int(len(nums) / 2)

        for i in nums:
            count[i] = count.get(i, 0) + 1
        
        for num in count:
            if count[num] > threshhold:
                return num