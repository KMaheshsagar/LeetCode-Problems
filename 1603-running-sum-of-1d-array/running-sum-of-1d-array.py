class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningsum=[]
        sums=0
        for i in range(len(nums)):
            sums+=nums[i]
            runningsum.append(sums)
        return runningsum


        