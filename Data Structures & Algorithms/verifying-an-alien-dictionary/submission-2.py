from collections import defaultdict
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ordering = defaultdict(int)

        for i, o in enumerate(order):
            ordering[o] = i
        
        i = 0
        while i < len(words)-1:
            word1 = words[i]
            word2 = words[i+1]

            minLen = min(len(word1), len(word2))
            j = 0

            flag = False
            while j < minLen:
                if ordering[word1[j]] > ordering[word2[j]]:
                    return False
                elif ordering[word1[j]] < ordering[word2[j]]:
                    flag = True
                    break
                j += 1
            
            if not flag and len(word1) > len(word2):
                return False
            
            i += 1
        
        return True