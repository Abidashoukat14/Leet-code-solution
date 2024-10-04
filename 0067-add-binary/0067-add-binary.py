class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans=[]
        remainder=0
        i=len(a)-1  
        j=len(b)-1   
        while i>=0 or j>=0 or remainder:
            if i>=0:
                remainder+=int(a[i])    
                i-=1
            if j>=0:   
                remainder+=int(b[j])     
                j-=1   
            ans.append(str(remainder%2))    
            remainder//=2   
        return ''.join(reversed(ans))