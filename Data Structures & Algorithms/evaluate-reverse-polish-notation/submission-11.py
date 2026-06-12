class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "*", "/", "-"]

        for c in tokens:
            if c in operators:
                num1 = stack.pop()
                num2 = stack.pop()

                if c == "+":
                    stack.append(num1+num2)
                
                elif c == "-":
                    stack.append(num2 - num1)
                
                elif c == "*":
                    stack.append(num1*num2)
                
                elif c == "/":
                    stack.append(int(num2/num1))
            else:
                stack.append(int(c))
        
        print(stack)
        return stack[-1]



