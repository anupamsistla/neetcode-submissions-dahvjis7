from collections import deque
class Solution:
    def predictPartyVictory(self, s: str) -> str:
        Radiant = deque()
        Dire = deque()

        for i in range(len(s)):
            if s[i] == 'R':
                Radiant.append(i)
            else:
                Dire.append(i)

        n = len(s)
        while Radiant and Dire:
            R, D = Radiant.popleft(), Dire.popleft()
            
            if R < D:
                Radiant.append(R + n)
            
            else:
                Dire.append(D+n)
        
        return "Radiant" if Radiant else "Dire"