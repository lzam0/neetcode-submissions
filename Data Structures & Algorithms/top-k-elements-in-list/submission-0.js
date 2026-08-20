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
        
        let sorted = Object.entries(val).sort((a, b) => b[1] - a[1]);
        let frequent = sorted.slice(0,k).map(item => Number(item[0]));

        return frequent;
    }
}
