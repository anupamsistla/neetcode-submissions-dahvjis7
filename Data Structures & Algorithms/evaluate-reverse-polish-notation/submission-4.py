class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        
        for t in tokens:
            if t == '+':
                a = nums.pop()
                b = nums.pop()
                ans = a + b
                nums.append(ans)
            elif t == '*':
                a = nums.pop()
                b = nums.pop()
                ans = a * b
                nums.append(ans)
            elif t == '-':
                a = nums.pop()
                b = nums.pop()
                ans = b-a
                nums.append(ans)
            elif t == '/':
                a = nums.pop()
                b = nums.pop()
                ans =int(b/a)
                nums.append(ans)
            else:
                nums.append(int(t))
        return nums[-1]