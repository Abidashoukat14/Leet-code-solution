class Solution:
    def sortColors(self, nums: List[int]) -> None:
        occurrence={}
        idx=0
        for i in range(len(nums)):
            occurrence[nums[i]]=occurrence.get(nums[i],0)+1
        for colors in range(3):
            t_present=occurrence.get(colors,0)
            nums[idx:idx+t_present] = [colors]*t_present
            idx+=t_present      
       



            
        