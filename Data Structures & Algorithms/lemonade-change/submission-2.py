class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten, twenty = 0, 0, 0

        for b in bills:
            if b == 5:
                five += 1
            
            elif b == 10:
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False
            
            else:
                res = b - 5
                if ten > 0:
                    ten -= 1
                    res -= 10
                
                while five > 0 and res > 0:
                    five -= 1
                    res -= 5

                if res:
                    return False    
                
                twenty += 1
        return True
            