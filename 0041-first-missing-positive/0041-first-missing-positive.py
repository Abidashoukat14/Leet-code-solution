class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums=[i for i in nums if i>0]
        nums.sort()
        minPosInterger=1
        for i in nums:
            if i==minPosInterger:
                minPosInterger+=1
            elif i>minPosInterger: 
                return minPosInterger   
        return minPosInterger
                         

       



        
        