class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        A,B = nums1, nums2
        m,n = len(A), len(B)

        total_left = (m+n+1)//2
        l,r = 0, m
        while l <= r:
            i = (l+r)//2
            j = total_left - i
            Aleft = float("-inf") if i == 0 else A[i-1]
            Aright = float("inf") if i == m else A[i]

            Bleft = float("-inf") if j == 0 else B[j-1]
            Bright = float("inf") if j == n else B[j]

            if Aleft <= Bright and Bleft <= Aright:
                if (m+n) %2 ==1:
                    return float(max(Aleft,Bleft))
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1



        
