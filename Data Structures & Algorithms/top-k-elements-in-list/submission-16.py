class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        res = []

        for f in nums:
            freqMap[f] = freqMap.get(f, 0) + 1
        
        bucket = [[] for _ in range(len(nums)+1)]

        for n in freqMap:
            bucket[freqMap[n]].append(n)
        
        i = len(bucket)-1
        while k > 0:
            if bucket and len(bucket[i]) <= k:
                res.extend(bucket[i])
                k -= len(bucket[i])
            elif bucket and len(bucket[i]) > k:
                start = len(bucket[i] - k)
                res.extend(bucket[i][start:])
                k = 0
            i -= 1
        return res
        