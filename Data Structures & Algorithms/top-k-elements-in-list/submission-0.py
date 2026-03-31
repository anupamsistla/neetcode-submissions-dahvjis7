class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for i in nums:
            count[i] = 1+ count.get(i, 0)

        frequency = [[] for i in range(len(nums)+1)]
        for i, j in count.items():
            frequency[j].append(i)
        
        final = []
        for i in range(len(frequency)-1, 0, -1):
            for j in frequency[i]:
                final.append(j)
                if len(final) == k:
                    return final

        