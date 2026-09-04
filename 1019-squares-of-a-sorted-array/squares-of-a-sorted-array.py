class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        sqlist=[0]*n
        l=0
        r=n-1
        p=n-1
        while l<=r:
            left_s=nums[l]**2
            right_s=nums[r]**2
            if left_s>=right_s:
                sqlist[p]=left_s
                l+=1
            else:
                sqlist[p]=right_s
                r-=1
            p-=1
        return sqlist
