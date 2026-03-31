class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listS = list(s)
        listT = list(t)
        listS = sorted(listS)
        listT = sorted(listT)
        return listS == listT
        