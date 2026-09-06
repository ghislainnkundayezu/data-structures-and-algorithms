class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = set(nums)
        max_seq = 0
        for n in nums:
            if n - 1 not in m:
                seq = 1
                c = n
                while c + 1 in m:
                    c += 1
                    seq += 1
                
                max_seq = max(max_seq, seq)

        return max_seq

        