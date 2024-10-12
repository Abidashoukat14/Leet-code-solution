class Solution:
    def isNumber(self, s: str) -> bool:
        integer_number=False
        exponent=False
        dot=False
        for idx,cur_val in enumerate(s):
            if cur_val.isdigit():
                integer_number=True
            elif cur_val in ('+','-'):
                if not (idx==0 or s[idx-1] in ('e','E')):
                    return False
            elif cur_val in ('e','E'):
                if exponent or not integer_number:
                    return False
                exponent=True
                integer_number=False
            elif cur_val=='.':
                if exponent or dot:
                    return False        
                dot=True   
            else:
                return False
        return integer_number



        




        
        