class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def validparenthesis(left,right,s):
            if len(s)==n*2:
                res.append(s)
                return 
            if left<n:
                validparenthesis(left+1,right,s+'(')
            if right<left:
                validparenthesis(left,right+1,s+')')
        res=[]  
        validparenthesis(0,0,'')
        return res     