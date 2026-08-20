class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        // make indicies = i = nums[i]
        var indicies = {};

        // hash mapped
        for(let i = 0; i < nums.length; i++){
            indicies[nums[i]] = i;
        }

        // loop through the entire array
        // essentially we want to do target - i
        // then we search through the hashmap if difference is found
        for(let i = 0; i < nums.length; i++){
            let diff = target - nums[i];
            console.log(diff);
            
            // check if the difference is 
            if(indicies[diff] !== undefined ){
                if(indicies[diff] !== i){
                    return [i, indicies[diff]];
                }
            }
        }

        return [];
    }
}
