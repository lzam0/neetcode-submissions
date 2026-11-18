class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # INPUT: strs = act, pots, tops, cat, stop, hat
        # OUTPUT: hat | act, cat | stop, pots, tops

        # extract individual words ***
        # sort the indivudal chars of a words ***
        # eg. act -> a c t -> act
        # eg 2. cat -> c a t -> act

        # if the sorted string is NOT inside of a hashmap already ***
        # then we can create a NEW grouping

        # OTHERWISE we can append to the grouping

        # return hashmap

        groups = {}

        for string in strs:
            sortString = tuple(sorted(string))

            # NEW GROUPINGS
            if sortString not in groups:
                groups[sortString] = [string]
            else:
                # APPEND TO GROUPS
                groups[sortString].append(string)

        return list(groups.values())