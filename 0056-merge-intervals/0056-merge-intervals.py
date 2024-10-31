class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        intervals.sort(key=lambda x:x[0])
        last= intervals[0]
        for current in intervals[1:]:
            if current[0] <= last[1]:
                last[1]=max(last[1],current[1])
            else:
                res.append(last) 
                last=current
        res.append(last)
        return res           