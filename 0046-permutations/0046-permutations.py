class Solution:
    def permutations(self,nums:list[int],idx:int,n:int,res:list[list[int]]):
        if idx==n:
            res.append(nums[:])
            return
        for i in range(idx,n+1):
            nums[idx],nums[i]=nums[i],nums[idx]
            self.permutations(nums,idx+1,n,res)
            nums[idx],nums[i]=nums[i],nums[idx]
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        self.permutations(nums,0,len(nums)-1,res)
        return res
       


        
        