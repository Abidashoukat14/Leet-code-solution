class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        heap={}
        for i in range(len(nums)):
            if nums[i] in heap and abs(i-heap[nums[i]])<=k:
                return True
            heap[nums[i]]=i
        return False        
        