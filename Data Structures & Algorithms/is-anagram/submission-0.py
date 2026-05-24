class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s)!= len(t)): return False
        dic = {}
        dic1 = {}
        for i in range(len(s)):
            dic[s[i]] = dic.get(s[i],0) + 1
            dic1[t[i]] = dic1.get(t[i],0) + 1
        return dic == dic1
            
