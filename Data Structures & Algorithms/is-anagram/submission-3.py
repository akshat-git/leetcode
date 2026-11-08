class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = {}
        td = {}
        if len(s) != len(t):
            return False
        else:
            for i in s:
                if i in sd.keys():
                    sd[i] += 1
                else:
                    sd[i] = 1
            for i in t:
                if i in td.keys():
                    td[i] += 1
                else:
                    td[i] = 1
        for i in td.keys():
            if i not in sd.keys() or sd[i]!= td[i]:
                return False
        return True
                
                
                    