class Solution:
    def countOnes(self, number):
        res = 0
        compare = 1
        while number > 0:
            res += number & compare
            number = number >> 1
        return res

    def countBits(self, n: int) -> List[int]:
        toRet = []
        for i in range(n + 1):
            toRet.append(self.countOnes(i))
        
        return toRet
