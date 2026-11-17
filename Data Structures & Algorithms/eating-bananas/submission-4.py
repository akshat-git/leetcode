import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)
        a = 1
        b = max(piles)
        while a<=b:
            m = (a+b)//2
            val = sum([math.ceil(x/m) for x in piles])
            if val <= h:
                b = m-1
            else:
                a = m+1
        return a
        