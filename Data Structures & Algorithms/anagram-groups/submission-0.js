class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        var result = {};

        // iterate through string strs arr
        for(let s of strs){

            // seperate the string so CAT is saved but then
            // reordered to ACT
            var sortedString = s.split('').sort().join('');
            
            if(!result[sortedString]){
                result[sortedString] = [];
            }
            result[sortedString].push(s);
        }
        return Object.values(result);
    }
}
