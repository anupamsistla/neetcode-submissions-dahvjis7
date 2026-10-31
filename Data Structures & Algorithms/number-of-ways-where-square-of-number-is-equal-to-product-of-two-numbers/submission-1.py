from collections import Counter
class Solution:
    def numTriplets(self, nums1: list[int], nums2: list[int]) -> int:
        freq1 = Counter(nums1)
        freq2 = Counter(nums2)
        res = 0

        for x in nums1:
            for a, ca in freq2.items():
                target = x ** 2
            
                if target % a != 0:
                    continue
                
                b = target // a

                if b not in freq2:
                    continue
                
                if a < b:
                    res += ca * freq2[b]
                
                elif a == b:
                    res += (ca * (ca - 1)) // 2
                
        for x in nums2:
            for a, ca in freq1.items():
                target = x ** 2
            
                if target % a != 0:
                    continue
                
                b = target // a

                if b not in freq1:
                    continue
                
                if a < b:
                    res += ca * freq1[b]
                
                elif a == b:
                    res += (ca * (ca - 1)) // 2
        
        return res