class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_occurrence={char:i for i,char in enumerate(s)}  
        res=[]
        in_res=set()
        for i ,char in enumerate(s):  
            if char in res:
                continue
            while res and char<res[-1]  and i<last_occurrence[res[-1]]:
                in_res.remove(res.pop()) 
            res.append(char) 
            in_res.add(char)      
        return ''.join(res)
        