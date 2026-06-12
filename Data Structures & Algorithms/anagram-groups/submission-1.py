class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        sot = strs.copy()
        sot.sort()
        for i in range(len(sot)):
            a = list(sot[i])
            a.sort()
            res[str(a)] = []

        for i in range(len(sot)):
            res[str(sorted(list(strs[i])))].append(strs[i])

        return list(res.values())



        
