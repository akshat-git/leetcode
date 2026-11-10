class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a = 0
        b = len(heights)-1
        m = 0
        while b>a:
            area = (b-a)*min(heights[a],heights[b])
            if area > m:
                m = area
            if heights[a]>heights[b]:
                b-=1
            elif heights[b]>=heights[a]:
                a+=1
        return m
