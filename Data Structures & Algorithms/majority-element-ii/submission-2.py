class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

            if len(count) > 2:
                for e in count:
                    count[e] -= 1
                
                for i, c in list(count.items()):
                    if c == 0:
                        count.pop(i)
        res = []
        for num in count:
            if nums.count(num) > len(nums) // 3:
                res.append(num)
        return res