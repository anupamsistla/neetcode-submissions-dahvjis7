class Solution:
    def countOnes(self, n):
        res = 0

        while n:
            n = n & (n-1)
            res += 1
        return res
    def countBits(self, n: int) -> List[int]:
        output = []

        for i in range(n+1):
            output.append(self.countOnes(i))
        return output