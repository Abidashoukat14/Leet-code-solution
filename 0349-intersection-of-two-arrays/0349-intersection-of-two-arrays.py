class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1=set(nums1)
        result=[]
        for num2 in nums2:
            if num2 in num1:
                result.append(num2)
                num1.remove(num2)
        return result        



        