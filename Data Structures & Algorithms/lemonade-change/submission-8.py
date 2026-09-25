class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0

        for b in bills:
            if b == 5:
                fives += 1
            
            elif b == 10:
                if fives == 0:
                    return False
                
                fives -= 1
                tens += 1
            
            else:
                toRet = 15
                if tens > 0:
                    toRet -= 10
                    tens -= 1
                
                if fives >= toRet // 5:
                    fives -= toRet // 5
                
                else:
                    return False
                
            
        return True
                
                