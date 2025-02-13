class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)    
        res=0
        for i in range(0,len(nums)):
            x=heapq.heappop(nums) 
            if x<k:
                res+=1
                y=heapq.heappop(nums) 
                if x<y:
                    value=x*2+y
                else:
                    value=y*2+x 
                heapq.heappush(nums,value) 
            else: 
                break 
        return res        


        