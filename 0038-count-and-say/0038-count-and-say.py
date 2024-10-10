class Solution:
    def countAndSay(self, n: int) -> str:
        def countTillDiff(s:str):
            ans=""
            i=0
            alt=''
            while i<len(s):
                count=1
                check=s[i]
                if (check==alt):
                    break
                alt= check
                for j in range (i+1,len(s)) :
                    if s[j]!=check:
                        i=j
                        break
                    count+=1
                    if j==len(s)-1:
                        i=j 
                        break
                ans+=str(count)+check
            return ans              
        if n==1:
            return "1"
        return countTillDiff(self.countAndSay(n-1))

        
       


        