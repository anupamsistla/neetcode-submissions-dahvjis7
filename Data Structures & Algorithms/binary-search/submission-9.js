class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number}
     */
    search(nums, target) {
        let l = 0;
        let r = nums.length-1;
        let mid = 0;

        while (l <= r){
            mid = Math.trunc((l+r)/2);
            
            if(nums[mid] === target){
                return mid;
            }

            else if(nums[mid] < target){
                l = mid + 1
            }

            else{
                r = mid - 1
            }
        }

        return -1;
    }
}
