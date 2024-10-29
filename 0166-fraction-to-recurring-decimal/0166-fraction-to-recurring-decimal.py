class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator==0: 
            return "0"
        sign="" if (numerator<0) == (denominator <0) else "-"
        numerator ,denominator = abs(numerator) , abs(denominator)
        intvalue= str(numerator // denominator)
        remainderIdx,starting,lastIdx,decimals,repeating ={},0,0,[],False
        if numerator % denominator ==0:
            return sign + intvalue
        while True:
            decimals.append(numerator // denominator)  
            remainder = numerator % denominator 
            numerator =remainder * 10
            if remainder ==0:
                repeating = False
                break
            if remainder in remainderIdx:
                repeating =True
                starting=remainderIdx[remainder]
                break
            remainderIdx[remainder]=lastIdx
            lastIdx+=1
        decimals=''.join(list(map(str,decimals[1:])))  
        if not repeating:
            return sign + intvalue + "."+ decimals 
        nonrepeatingPart=decimals[:starting]  
        repeatingPart=decimals[starting:lastIdx]    
        return sign + intvalue + "." + nonrepeatingPart + f"({repeatingPart})"


        