class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        // create a indicies hashmap
        // val -> index
        var indicies = {};
        
        for(var i = 0; i < nums.length; i++){
            indicies[nums[i]] = i;
        }

        // iterate through the entire array
        // diff target - index value
        // then check the hashmap if that value is present
        // if present then print result otherwise no result

        for(var i = 0; i < nums.length; i++){
            var diff = target - nums[i];

            // checking if the indicies diff is inside of hashmap
            if(indicies[diff] !== undefined){
                // check if it isnt index i
                if(indicies[diff] !== i){
                    return [i, indicies[diff]];
                }
            }
        }
        return [];
    }
}
