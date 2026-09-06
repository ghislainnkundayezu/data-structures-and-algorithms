class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n
        output = [0] * n

        prefix[0] = postfix[n - 1] = 1

        # build the prefix array
        for i in range(1, n):
            prefix[i] = nums[i-1] * prefix[i-1]

        for y in range(n-2, -1, -1):
            postfix[y] = nums[y+1] * postfix[y+1]

        for x in range(n):
            output[x] = prefix[x] * postfix[x]
            print(output)
        print(postfix)
        print(output)
        return output