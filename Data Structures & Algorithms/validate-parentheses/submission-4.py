class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c == "(":
                stack.append(")")
            elif c == "[":
                stack.append("]")
            
            elif c == "{":
                stack.append("}")

            elif c == ")":
                if stack and stack[-1] == c:
                    stack.pop()
                else:
                    return False
                
            elif c == "]":
                if stack and stack[-1] == c:
                    stack.pop()
                else:
                    return False
                
            elif c == "}":
                if stack and stack[-1] == c:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        else:
            return False