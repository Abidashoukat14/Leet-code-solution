class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack=[]
        for digits in num:
            while stack and k>0 and digits<stack[-1]:
                stack.pop()
                k-=1
            stack.append(digits)
        if k>0:
            stack=stack[:-k] 
        else:
            stack  
        ans=''.join(stack).lstrip('0')
        if ans:
            return ans
        else:
            return '0'      

        