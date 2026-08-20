class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        let val = {};

        // iterate through the entire array
        // if its a new value then add to val hashmap and give it value 1
        // otherwise increment the current value
        for(let i = 0; i < nums.length; i++){
            
            
            if(val[nums[i]] === undefined){
                val[nums[i]] = 1;
            }else{
                val[nums[i]] += 1;
            }
        }

        // check if the object has a dup
        for(const [key, count] of Object.entries(val)){
            if(count > 1){
                return true;
            }
        }
        return false;
    }
}
