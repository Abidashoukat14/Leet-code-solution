class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        letterCombinations={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }   
        def find_combination(idx,comb):
            if idx==len(digits):
                res.append(comb[:])
                return
            for i in letterCombinations[digits[idx]]:
                find_combination(idx+1,comb+i)
        res=[] 
        find_combination(0,"")
        return res       