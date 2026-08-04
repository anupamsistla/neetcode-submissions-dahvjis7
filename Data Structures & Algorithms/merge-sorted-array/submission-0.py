class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = nums1[:m]
        right = nums2
        i, L, R = 0, 0, 0

        while L < len(left) and R < len(right):
            if left[L] <= right[R]:
                nums1[i] = left[L]
                L += 1
            
            else:
                nums1[i] = right[R]
                R += 1

            i += 1
  
        while L < len(left):
            nums1[i] = left[L]
            i += 1
            L += 1
        
        while R < len(right):
            nums1[i] = right[R]
            i += 1
            R += 1
        
        return 
    
