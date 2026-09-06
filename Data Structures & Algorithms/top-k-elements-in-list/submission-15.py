class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        res = []

        for n in nums:
            freqMap[n] = freqMap.get(n, 0) + 1
        
        freqRank = list(freqMap.items())
        freqRank.sort(reverse=True, key=lambda r: r[1])

        for i in range(k):
            res.append(freqRank[i][0])
        
        return res