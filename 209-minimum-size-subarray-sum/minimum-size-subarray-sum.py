class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        length=0
        sums=0
        minlen=float('inf')
        for r in range(len(nums)):
            sums+=nums[r]
            while sums>=target:
                minlen=min(minlen,r-l+1)
                sums-=nums[l]
                l+=1
        return minlen if minlen!=float('inf') else 0