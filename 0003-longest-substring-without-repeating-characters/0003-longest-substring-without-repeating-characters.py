class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lon_length=0
        n=len(s)
        str_idx=[-1]*128
        left=0
        for i in range(n):
            if str_idx[ord(s[i])]>=left:
                left=str_idx[ord(s[i])]+1
            str_idx[ord(s[i])]=i
            lon_length=max(lon_length,i-left+1)    
        return lon_length 

            
               
       