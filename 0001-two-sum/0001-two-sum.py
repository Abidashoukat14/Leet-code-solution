class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create hashmap for storing values with indexs
        hashmap={}  
        #start a loop from 0 index to last index for search numbers whose sum equal to target 
        for i in range(len(nums)):
            # get second number which we have to search  
            secNum= target - nums[i] 
            # check the second number is in hashmap or not if it is then return indexs of both numbers if this sec num present given nums or not 
            if secNum in hashmap:
                return [hashmap[secNum],i]
            # if second number is not in hashmap means if this num is in nums or not if it is return indexes otherwise add it in hashmap     
            else:
                hashmap[nums[i]]=i    
    
    