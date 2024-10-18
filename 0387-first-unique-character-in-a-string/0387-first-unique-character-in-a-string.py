class Solution:
    def firstUniqChar(self, s: str) -> int:
        map = {}
        for val in s:
            if val in map:
                map[val] += 1
            else:
                map[val] = 1
        for i in range(len(s)):
            if map[s[i]] == 1:
                return i
        return -1 
               
            

        