class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for s in strs:
            key = "".join(sorted(s))
            anagrams[key] = anagrams.get(key,[]) + [s]

        return list(anagrams.values())
            