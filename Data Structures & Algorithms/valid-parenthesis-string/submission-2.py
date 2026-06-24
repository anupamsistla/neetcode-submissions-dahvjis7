class Solution:
    def checkValidString(self, s: str) -> bool:
        leftParen = []
        star = []

        for i in range(len(s)):
            if s[i] == '(':
                leftParen.append(i)
            
            elif s[i] == "*":
                star.append(i)
            
            elif s[i] == ')':
                if leftParen:
                    leftParen.pop()
                
                elif star:
                    star.pop()
                
                else:
                    return False
            
        # if len(leftParen) > len(star):
        #     return False
        
        # elif leftParen and star and leftParen[-1] > star[-1]:
        #     return False
        
        # else:
        #     return True
    
        minLen = min(len(leftParen), len(star))
        for i in range(minLen):
            leftI, starI = leftParen.pop(), star.pop()

            if leftI > starI:
                return False

        if leftParen:
            return False
        
        return True

        # after all iterations return false if number of left parentheses is more than the number of stars available
                    