class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result=[1]
        prev_row=1
        for i in range(1,rowIndex +1):
            cur_row= prev_row *(rowIndex - i +1)//i
            result.append(cur_row)
            prev_row = cur_row
        return result   

              





       




        