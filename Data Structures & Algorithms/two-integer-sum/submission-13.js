class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        var vals = {};

        // increment the nums into vals object
        for(let i = 0; i < nums.length; i++){
            vals[nums[i]] = i;
        }

        // now lets do difference = target - i
        // if diff is inside of vals object
        // return [i, diff]
        for(let i = 0; i < nums.length; i++){
            let diff = target - nums[i];
            console.log(nums[i])
            // check if the differnece is inside the object
            if(vals[diff] !== undefined){ // is inside of vals
                if(vals[diff] !== i){ // check if difference isnt currently i
                    return [i, vals[diff]];
                }
            }
        }

        return [];
    }
}
