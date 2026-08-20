class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {
        let val = {};

        for(let i = 0; i < nums.length; i++){
            if(val[nums[i]] === undefined){
                val[nums[i]] = 1
            }else{
                val[nums[i]] += 1
            }
        }
        
        // sort the object largest val on top
        let sorted = Object.entries(val).sort((a, b) => b[1] - a[1]);
        
        // then slice the sorted obj to key length and get the keys
        let frequent = sorted.slice(0,k).map(item => Number(item[0]));

        return frequent;
    }
}
