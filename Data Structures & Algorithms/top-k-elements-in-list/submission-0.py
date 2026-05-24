class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1

        sortdic = sorted(dic,key = dic.get, reverse = True)

        return sortdic[:k]


            
        