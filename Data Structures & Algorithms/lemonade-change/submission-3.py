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
                change = 15

                if ten > 0:
                    ten -= 1
                    change = 5

                if change == 5 and five > 0:
                    five -= 1
                
                elif change == 15 and five >= 3:
                    five -= 3
                
                else:
                    return False
        return True
            