class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        hamsters = list(hamsters)
        res = 0

        for i in range(len(hamsters)):
            if hamsters[i] == "H":
                if hamsters[i-1] == "B":
                    continue
            
                flag = False

                if i < len(hamsters)-1 and hamsters[i+1] == ".":
                    hamsters[i+1] = "B"
                    res += 1
                    flag = True
                
                elif i >= 1 and hamsters[i-1] == "." and hamsters[i] == "H":
                    hamsters[i-1] = "B"
                    res += 1
                    flag = True

                if not flag:
                    return -1

        return res