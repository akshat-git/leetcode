class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq.keys():
                freq[i] = 0
            freq[i]+=1
        buckets = [[] for i in range(len(nums))]
        for n in freq:
            buckets[freq[n]-1].append(n)
        l = 0
        out = []
        for i in range(len(buckets)):
            
            if buckets[-1*i-1] == []:
                pass
            else:
                print(buckets[-1*i-1])
                for j in range(len(buckets[-1*i-1])):
                    print(j, buckets[-1*i-1][j])
                    if l == k:
                        return out
                    else:
                        out.append(buckets[-1*i-1][j])
                        l+=1
        return out


        

        