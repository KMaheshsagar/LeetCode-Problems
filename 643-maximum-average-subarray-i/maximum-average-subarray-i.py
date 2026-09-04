class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l=0
        maxiavg=float('-inf')
        sums=0
        for r in range(len(nums)):
            sums+=nums[r]
            if (r-l+1)==k:
                maxiavg=max(maxiavg,(sums/k))
                sums-=nums[l]
                l+=1
        return maxiavg
        