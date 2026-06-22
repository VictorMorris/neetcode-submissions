class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numCnt = {}
        for num in nums:
            numCnt[num] = numCnt.get(num, 0) + 1

        longest = 0
        for num, cnt in numCnt.items():
            sequence = []
            if numCnt.get(num-1, 0) == 0:
                sequence.append(num)
                t = num + 1
                while True:
                    if numCnt.get(t, 0) != 0:
                        sequence.append(t)
                        t += 1
                    else:
                        break
            if len(sequence) > longest:
                longest = len(sequence)
        return longest

        