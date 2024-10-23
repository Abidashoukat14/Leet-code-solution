class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_sum=0
        t_sum=0
        for i in s:
            s_sum+=ord(i)
        for j in t:
            t_sum+=ord(j)    
        difference=t_sum-s_sum
        return chr(difference)
        