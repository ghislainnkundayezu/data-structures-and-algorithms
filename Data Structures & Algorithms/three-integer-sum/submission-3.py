class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums) - 1
        result = []
        for i in range(n):

            if (i - 1) >= 0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            k = n

            while j < k:
                sum_ = nums[i] + nums[j] + nums[k]
                if sum_ < 0:
                    j += 1
                elif sum_ > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1 
                 

        return result        

