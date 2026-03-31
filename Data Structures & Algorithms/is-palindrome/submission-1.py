class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        original = ""
        for c in s:
            if(c.isalnum()):
                original +=c
        return original == original[::-1]

    