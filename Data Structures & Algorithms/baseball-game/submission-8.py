class Solution:
    def calPoints(self, operations: List[str]) -> int:

        score = []

        for i in range(len(operations)):
            value = operations[i]

            if value == "+":
                # Record a new score that is the sum of the previous two scores.
                newVal = int(score[-1]) + int(score[-2])
                score.append(newVal)
            elif value == "D":
                # get the most recent value of the stack and double it 
                newVal = int(score[-1]) * 2
                score.append(newVal)
            elif value == "C":
                # remove most recent value added to score
                score.pop()
            else:
                score.append(int(value))

        # return the score sum
        return sum(score)