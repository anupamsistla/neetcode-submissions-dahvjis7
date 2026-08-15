class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count5, count10, count20 = 0, 0, 0

        for i in range(len(bills)):
            if bills[i] == 5:
                count5 += 1
            
            elif bills[i] == 10:
                if count5 > 0:
                    count5 -= 1
                else:
                    return False
                count10 += 1
                
            elif bills[i] == 20:
                change = 15

                if count10 > 0:
                    count10 -= 1
                    change = 5
                
                if count5 > 0:
                    if change == 5:
                        change = 0
                        count5 -= 1
                    
                    elif change == 15:
                        if count5 < 3:
                            return False
                        
                        else:
                            change = 0
                            count5 -= 3
                else:
                    return False
        return True
                