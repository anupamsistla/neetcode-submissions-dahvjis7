from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # charCount = defaultdict(list)
        # for s in strs:
        #     count = [0]*26
        #     for c in s:
        #         count[ord(c)-ord("a")] +=1

        #     charCount[tuple(count)].append(s)
        # return charCount.values()

        charCount = defaultdict(list)
        for s in strs:
            key = tuple(sorted(Counter(s).items()))
            charCount[key].append(s)
        return charCount.values()


                    

