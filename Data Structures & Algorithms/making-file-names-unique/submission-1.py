from collections import defaultdict
class Solution:
    def getFolderNames(self, names: list[str]) -> list[str]:
        lastSuffix = {}

        for name in names:
            if name not in lastSuffix:
                lastSuffix[name] = 1
            
            else:
                k = lastSuffix[name]
                modified = f"{name}({k})"

                while modified in lastSuffix:
                    k += 1
                    modified = f"{name}({k})"
                
                lastSuffix[name] = k + 1
                lastSuffix[modified] = 1
            
        return list(lastSuffix.keys())