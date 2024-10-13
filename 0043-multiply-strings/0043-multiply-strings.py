class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=='0':
            return '0'
        len_num1,len_num2=len(num1),len(num2)
        output=[0]*(len_num1+len_num2)
        for i in range(len_num1-1,-1,-1):
            for j in range(len_num2-1,-1,-1):
                product=(ord(num1[i])- ord('0'))*(ord(num2[j])- ord('0'))
                left=i+j
                right=i+j+1
                carry=product+output[right]
                output[right]=carry%10
                output[left]+=carry//10
        result=''.join(map(str,output)) 
        return result.lstrip('0')     

        
        