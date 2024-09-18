class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
          return self.binarysearch(nums,target,0,len(nums)-1)
    def binarysearch(self,nums: List[int], target: int,left:int,right:int)->int:
        if left>right:
            return left
        mid=(left+right)//2
        mid_value=nums[mid]
        if mid_value==target:
            return mid
        if mid_value<target:
            return self.binarysearch(nums,target,mid+1,right)
        else:
            return self.binarysearch(nums,target,left,mid-1)
               
              

                        
        