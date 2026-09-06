class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_map = {}
        bucket = [[] for i in range(len(nums) + 1)]
        result = []
        print(bucket)
        for num in nums:
            nums_map[num] = nums_map.get(num, 0) + 1
        
        for n, f in nums_map.items():
             
            #print(nums_map[f])
            bucket[f].append(n)
        
        while len(result) <= k-1 and bucket:
            last = bucket.pop()

            if (last):
                result.extend(last)
                print("l", len(result), last)


        print(nums_map)
        print(bucket) 
        print(result)
        return result