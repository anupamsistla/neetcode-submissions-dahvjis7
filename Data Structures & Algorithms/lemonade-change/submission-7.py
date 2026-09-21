class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = 0
        tens = 0
    
        for b in bills:
            if b == 5:
                fives += 1
            
            elif b == 10:
                tens += 1
                if fives > 0:
                    fives -= 1
                
                else:
                    return False
                
            elif b == 20:
                currTotal = 15
                if tens > 0:
                    tens -= 1
                    currTotal -= 10
                
                fivesReq = currTotal // 5

                if fivesReq <= fives:
                    fives -= fivesReq
                
                else:
                    return False
                

        
        return True
