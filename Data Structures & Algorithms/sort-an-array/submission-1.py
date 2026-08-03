class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(L, R, M, nums):
            left = nums[L:M+1]
            right = nums[M+1:R+1]
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    nums[i] = left[j]
                    j += 1
                
                else:
                    nums[i] = right[k]
                    k += 1
                i += 1
            
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1
            
            return nums
        
        def mergeSort(l, r, nums):
            if l == r:
                return nums
            
            mid = (l+r)//2
            mergeSort(l, mid, nums)
            mergeSort(mid + 1, r, nums)
            merge(l, r, mid, nums)
            return nums
        
        return mergeSort(0, len(nums)-1, nums)