class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p1s=p2t=0
        while p2t<len(t):
            if p1s<len(s) and s[p1s]==t[p2t]:
                p1s+=1
            p2t+=1    
        return p1s==len(s)
        
        
        
            



        