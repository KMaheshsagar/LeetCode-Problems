class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        newlist=[]
        for i in range(len(nums)):
            if i>0 and nums[i-1]==nums[i]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                total=nums[i]+nums[l]+nums[r]
                if total==0:
                    newlist.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l-1]==nums[l]:
                        l+=1
                    while l<r and  r+1 <len(nums) and nums[r]==nums[r+1]:
                        r+=1
                elif total<0:
                    l+=1
                else:
                    r-=1
        return newlist        