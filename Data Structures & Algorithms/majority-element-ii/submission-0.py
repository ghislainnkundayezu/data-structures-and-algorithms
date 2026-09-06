class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        threshold = int(len(nums)/3)
        res = set()
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
            if count[n] > threshold:
                res.add(n)
        return list(res)
