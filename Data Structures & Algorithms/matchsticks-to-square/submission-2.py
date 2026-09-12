class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sides = [0]*4
        matchsticks.sort(reverse=True)
    
        currSum = sum(matchsticks)

        if currSum % 4:
            return False

        length = currSum // 4
        sides = [0]*4

        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if backtrack(i+1): return True
                    sides[j] -= matchsticks[i]
            return False
        
        return backtrack(0)
        

