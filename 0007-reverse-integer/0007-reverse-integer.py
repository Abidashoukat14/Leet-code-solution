class Solution:
    def reverse(self, x: int) -> int:
        rev=0
        if x<0:
            sign=-1
        else:
            sign=1    
        x=abs(x)
        while x!=0:
            last_digit=x%10
            rev=rev*10+last_digit
            x=x//10
        rev*=sign
        if rev>2**31-1 or rev<-2**31:
            return 0
        return rev

        
        