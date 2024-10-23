class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sumOf_s=sumOf_t=0
        for i in t:
            sumOf_t+=ord(i)
        for j in s:
            sumOf_s+=ord(j)   
        random_letter=sumOf_t-sumOf_s
        return  chr(random_letter)    
            
        