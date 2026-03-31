class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        track = defaultdict(int)
        
        for i in range(len(numbers)):
            search = target - numbers[i]
            if track[search]:
                return [track[search], i +1]
            track[numbers[i]] = i + 1;
        return []
                
            
                
