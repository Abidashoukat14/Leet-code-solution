class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        totalChalk=sum(chalk)
        remainingChalk=k%totalChalk
        for index, useChalk in enumerate(chalk):
            if remainingChalk <useChalk:
                return index
            remainingChalk-= useChalk 
        return 0                   

        