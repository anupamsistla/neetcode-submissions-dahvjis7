class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ["+", "-", "/", "*"]

        for t in tokens:
            if t not in operations:
                stack.append(t)
            else:
                a = int(stack.pop())
                b = int(stack.pop())
                if t == "+":
                    stack.append(a+b)
                elif t == "-":
                    stack.append(b-a)

                elif t == "/":
                    stack.append(b/a)

                elif t == "*":
                    stack.append(b*a)
        
        return int(stack[-1])