class Solution:
    def findLatestTime(self, s: str) -> str:
        first, second, third, fourth = s[0], s[1], s[3], s[4]
        
        if first == "?":
            if second == "?":
                first = "1"
                second = "1"

            else:
                if ord(second) > ord("1"):
                    first = "0"
                
                else:
                    first = "1"
        
        if second == "?":
            if first == "0":
                second = "9"
            
            else:
                second = "1"
            
        
        if third == "?":
            third = "5"
        

        if fourth == "?":
            fourth = "9"

        return f"{first}{second}:{third}{fourth}"