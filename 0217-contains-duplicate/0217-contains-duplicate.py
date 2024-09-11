class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate={}
        for n in nums:
            if n in duplicate:
                return True
            duplicate[n]=1
        return False    
        