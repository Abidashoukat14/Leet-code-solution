class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        def reverseSolution(left,right):
            while left<right:
                nums[left],nums[right] =nums[right],nums[left]
                left+=1
                right-=1
        reverseSolution(0,len(nums)-1)
        reverseSolution(0,k-1)
        reverseSolution(k,len(nums)-1)        