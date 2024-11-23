class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        m, n = len(box), len(box[0])
        for row in box:
            write_pos = n - 1 
            for j in range(n - 1, -1, -1):
                if row[j] == '#': 
                    row[j] = '.'
                    row[write_pos] = '#'
                    write_pos -= 1
                elif row[j] == '*': 
                    write_pos = j - 1
        rotated_box = [[box[i][j] for i in range(m - 1, -1, -1)] for j in range(n)]
        return rotated_box

     

        