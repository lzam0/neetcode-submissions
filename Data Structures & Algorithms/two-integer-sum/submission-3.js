class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        for(var i = 0; i < nums.length; i++){
            for(var j = i + 1; j < nums.length; j++){
                var total = nums[i] + nums[j];
                if(total === target){
                    return [i, j];
                }
            }
        }
        return [];
    }
}
