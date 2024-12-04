class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        res=[-1] * (n+1)
        for num in nums:
            res[num] = num
        for i in range(len(res)):
            if res[i]== -1:
                return i
        return 0        