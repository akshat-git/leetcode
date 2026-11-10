class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        starts = set()
        for i in numset:
            if i-1 not in numset:
                starts.add(i)
        m = 0
        for i in starts:
            count = 1
            k=i
            while k+1 in numset:
                count+=1
                k+=1
            if count > m:
                m = count
        return m
            
            
