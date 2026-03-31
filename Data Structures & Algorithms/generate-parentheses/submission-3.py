class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def paren(openN, closedN):
            if(openN == closedN == n):
                res.append("".join(stack))
                return
            
            if(openN < n):
                stack.append("(")
                paren(openN + 1, closedN)
                stack.pop()

            if(closedN < openN):
                stack.append(")")
                paren(openN, closedN+1)
                stack.pop()
        paren(0,0)
        return res