class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        score = []

        for curr in range(len(operations)):
            if operations[curr] == "+":
                # append a new score that is the sum of the previous two scores
                add = int(score[-1]) + int(score[-2])
                score.append(add)

            elif operations[curr] == "D":
                # record a new score that is double the previous score
                double = int(score[-1]) * 2
                score.append(double)

            elif operations[curr] == "C":
                # invalidate the previous score remvoing it from the record stack
                score.pop()
            else:
                # add it to the stack of score
                score.append(int(operations[curr]))

        # return the sum of the operations
        return sum(score)