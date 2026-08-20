class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let vals = {};

        for(let i = 0; i < nums.length; i++){
            if(vals[nums[i]] === undefined){
               vals[nums[i]] = 1; 
            } else{
                vals[nums[i]] += 1;
            }

        }

        for(const [key, count] of Object.entries(vals)){
            if(count > 1){
                return true;
            }
        }
        return false;
    }
}
