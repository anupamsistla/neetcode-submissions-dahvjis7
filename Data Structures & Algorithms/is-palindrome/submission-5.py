class Solution:
    def isPalindrome(self, s: str) -> bool:
        #left and right pointer meet in the middle where left = right lol
        l,r = 0, len(s)-1

        while l < r:
            while not s[l].isalnum() and l < r:
                l+=1
            
            while not s[r].isalnum() and r > l:
                r-=1

            if not s[l].lower() == s[r].lower():
                return False
            else:
                l += 1
                r-=1
        return True
        