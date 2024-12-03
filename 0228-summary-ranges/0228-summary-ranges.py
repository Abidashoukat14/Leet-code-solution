class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) < 1:
            return []
        result=[]
        left,right=0,1   
        while right<len(nums): 
            if nums[right] != nums[right-1]+1:
                if nums[right-1]==nums[left]:
                    result.append(f"{nums[left]}")
                else:
                    result.append(f"{nums[left]}->{nums[right-1]}") 
                left=right
            right+=1
        if left<len(nums):
            if nums[right-1]==nums[left]:
                result.append(f"{nums[left]}") 
            else:
                result.append(f"{nums[left]}->{nums[right-1]}")                  
        return result
            



        