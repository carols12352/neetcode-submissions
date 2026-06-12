class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        res = sorted(cnt.items(),key=lambda x:x[1], reverse=True)
        return [item[0] for item in res[:k]]
        # return list(res[:k][0])