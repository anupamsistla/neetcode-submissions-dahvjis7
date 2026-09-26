class Solution:
    def checkValidString(self, s: str) -> bool:
        leftParen = []
        wildCard = []

        for i in range(len(s)):
            if s[i] == "(":
                leftParen.append(i)
            
            elif s[i] == "*":
                wildCard.append(i)

            else:
                if leftParen:
                    leftParen.pop()
                
                else:
                    if wildCard:
                        wildCard.pop()

                    else:
                        return False
        
        while leftParen and wildCard:
            l, w = leftParen.pop(), wildCard.pop()

            if w < l:
                return False
            
        return len(leftParen) == 0