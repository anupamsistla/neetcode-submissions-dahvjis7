class Solution:
    def foo(self, i, n, k, curr, res):
        if k == 0:
            res.append(curr.copy())
            return 

        if i > n:
            return 

        curr.append(i)
        self.foo(i+1, n, k-1, curr, res)
        curr.pop()
        self.foo(i+1, n, k, curr, res)
        return 
        
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.foo(1, n, k, [], res)

        return res
