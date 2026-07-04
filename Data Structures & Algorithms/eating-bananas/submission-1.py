class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper = max(piles)
        lower = 1
        res = 0

        while lower <= upper:
            k = lower + ((upper - lower) // 2)
            time = 0

            for pile in piles:
                time += math.ceil(float(pile) / k)
            
            if time <= h:
                upper = k - 1
                res = k
            else:
                lower = k + 1

        return res
            