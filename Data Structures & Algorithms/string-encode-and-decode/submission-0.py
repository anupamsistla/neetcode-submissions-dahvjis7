class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        skip = "#"
        for s in strs:
            res = res + str(len(s)) + skip + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            lenght = int(s[i:j])
            i = j + 1
            j = i + lenght
            res.append(s[i:j])
            i = j
        return res


