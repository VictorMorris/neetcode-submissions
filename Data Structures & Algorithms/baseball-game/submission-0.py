class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = collections.deque()

        for op in operations:
            if op == "+":
                score1 = record.pop()
                score2 = record.pop()
                score3 = score1 + score2
                record.append(score2)
                record.append(score1)
                record.append(score3)
            elif op == "C":
                record.pop()
            elif op == "D":
                score = record.pop()
                record.append(score)
                record.append(2*score)
            else:
                record.append(int(op))

        return sum(record)