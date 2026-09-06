class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1
        
        bucket  = [[] for _ in range(len(nums)+1)]
        print(bucket)
        for item, count in num_freq.items():
            print(count)
            bucket[count].append(item)

        
        res = []

        for i in range(len(bucket)-1, 0, -1):
            for n in bucket[i]:
                print(n, res)
                if len(res) < k:
                    res.append(n)
        return res
