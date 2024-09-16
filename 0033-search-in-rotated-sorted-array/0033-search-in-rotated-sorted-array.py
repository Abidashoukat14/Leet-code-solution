class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)
        while left<right:
            if len(nums)==1 and nums[0]==target:
                return 0
            if nums[left]==target:
                return left
            else:
                left+=1
        return -1           
                       
           
        

        