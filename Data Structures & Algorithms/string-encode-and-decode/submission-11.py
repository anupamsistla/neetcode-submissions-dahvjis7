class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            step = s[i: j]
            i += len(str(step)) + 1
            end = i + int(step)
            res.append(s[i : i + int(step)])
            i = end
        return res
            

