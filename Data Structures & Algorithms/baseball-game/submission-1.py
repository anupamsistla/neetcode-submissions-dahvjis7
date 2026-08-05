class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            
            if op == "D":
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
            
            else:
                stack.append(int(op))
            
        toRet = 0
        while stack:
            toRet += stack.pop()
        
        return toRet