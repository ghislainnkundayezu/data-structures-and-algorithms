class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        freq = list(count.items())
        freq.sort(key=lambda x: x[1])

        res = []

        for k in range(k):
            res.append(freq.pop()[0])
        
        return res