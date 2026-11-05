class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        i,j=0,1
        res=[0]*len(nums)
        for x in nums:
            if x>0:
                res[i]=x
                i+=2
            else:
                res[j]=x
                j+=2
        return res
                
        