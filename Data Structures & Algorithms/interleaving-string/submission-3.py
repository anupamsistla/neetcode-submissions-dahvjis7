class Solution:
    def foo(self, i, j, k, s1, s2, s3):
        if i < 0 and j < 0 and k < 0:
            return True
        
        if k < 0:
            return False

        if i >= 0 and s1[i] == s3[k]:
            return self.foo(i-1, j, k-1, s1, s2, s3)
        
        if j >=0 and s2[j] == s3[k]:
            return self.foo(i, j-1, k-1, s1, s2, s3)
        
        return False

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        k = len(s3)
        return self.foo(n-1, m-1, k-1, s1, s2, s3)

        