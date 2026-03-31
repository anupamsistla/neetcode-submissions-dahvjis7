class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = ""

        for c in s:
            if(c.isalnum()):
                res = res + c
        return res == res[::-1]