from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        R, D = deque(), deque()
        
        for i, c in enumerate(senate):
            if c == "R":
                R.append(i)
            
            else:
                D.append(i)

        n = len(senate)

        while R and D:
            r = R.popleft()
            d = D.popleft()

            if r < d:
                R.append(r + n)
            
            else:
                D.append(d + n)
            
        return "Radiant" if R else "Dire"