class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freqs = {}
        for w in strs:
            count = [0]*26
            for c in w:
                count[ord(c)-ord("a")]+=1
            key = tuple(count)
            if key not in freqs:
                freqs[key] = []
            freqs[key].append(w)
        return list(freqs.values())
                
                