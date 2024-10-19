class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry=0
        res=[]
        n1,n2=len(num1)-1,len(num2)-1
        while n1>=0 or n2>=0 or carry:
            if n1>=0:
                digit=ord(num1[n1])-ord('0')
            else:
                digit=0    
            if n2>=0:
                digit2=ord(num2[n2])-ord('0')
            else:
                digit2=0 
            sum=digit+digit2+carry
            carry=sum//10
            res.append(str(sum%10))
            n1-=1
            n2-=1
        return ''.join(res[::-1])

        