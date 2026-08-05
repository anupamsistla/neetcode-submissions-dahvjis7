class Solution:
    def isInt(self, check):
        try:
            int(check)
            return True

        except ValueError:
            return False

    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if self.isInt(op):
                stack.append(int(op))
            
            elif op == "D":
                if stack:
                    top = stack[-1]
                    stack.append(top*2)
                
            elif op == "C":
                if stack:
                    stack.pop()
            
            elif op == "+":
                if len(stack) >= 2:
                    one, two = stack[-1], stack[-2]
                    stack.append(one + two)
            
        toRet = 0
        while stack:
            toRet += stack.pop()
        
        return toRet