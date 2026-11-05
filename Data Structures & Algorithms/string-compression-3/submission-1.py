class Solution:
    def compressedString(self, word: str) -> str:
        comp = []
        prev = None
        i = 0

        while i < len(word):
            if not prev:
                prev = word[i]
                count = 1
            
            else:
                if prev != word[i]:
                    comp.append(str(count))
                    comp.append(prev)
                    prev = word[i]
                    count = 1
                
                else:
                    count += 1
                    if count == 9:
                        comp.append(str(count))
                        comp.append(prev)
                        prev = None
    
            i += 1

        if prev:    
            comp.append(str(count))
            comp.append(prev)
        
        return "".join(comp)

                    