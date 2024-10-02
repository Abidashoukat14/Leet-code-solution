class Solution:
    def isValid(self, s: str) -> bool:
        ans=[]
        for i in range(len(s)):
            if ans:
                last=ans[-1]
                if self.ispair(last,s[i]):
                    ans.pop()
                    continue
            ans.append(s[i]) 
        return not ans            
    def ispair(self,last,cur):
        if last=="(" and cur==")" or last=="{" and cur=="}" or last=="[" and cur=="]":
            return True
        return False    



        

            
        