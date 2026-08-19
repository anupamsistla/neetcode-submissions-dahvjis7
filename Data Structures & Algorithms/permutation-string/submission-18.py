class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        countS1 = [0]*26
        for c in s1:
            countS1[ord(c)-ord("a")] += 1

        check = [0]*26

        l,r = 0,0

        while r < len(s2):
            check[ord(s2[r]) - ord("a")] += 1

            if check == countS1:
                return True

            if r-l+1 == len(s1):
                check[ord(s2[l]) - ord("a")] -= 1
                l += 1

            r += 1
        
        return False
            