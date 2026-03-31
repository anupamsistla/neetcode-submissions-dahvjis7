class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p, s in zip(position, speed)]

        stack = []

        for p, s in sorted(pair)[::-1]:
            res = (target-p)/s
            if not stack:
                stack.append(res)
            if stack and res > stack[-1]:
                stack.append(res)
        
        return len(stack)
            