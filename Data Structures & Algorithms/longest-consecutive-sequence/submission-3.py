class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums)
        max_seq = 0
        for n in nums:
            if n - 1 not in m:
                length = 1
                
                while n + length in m:
                    
                    length += 1
                
                max_seq = max(max_seq, length)

        return max_seq

        