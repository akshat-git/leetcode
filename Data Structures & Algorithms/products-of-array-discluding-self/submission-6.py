class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        z = set()
        tot = 0
        for i in nums:
            if i != 0:
                tot = 1

        for i in range(len(nums)):
            if nums[i] == 0:
                z.add(i)
            else:
                tot *= nums[i]
        out = []
        if len(z) > 1:
            return [0]*len(nums)
        print(z, tot)
        for i in nums:
            if len(z) and i != 0:
                out.append(0)
            elif i == 0:
                out.append(tot)
            else:
                out.append(int(tot/i))
        return out

