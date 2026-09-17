class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        res=[]
        A_mini=float('inf')
        B_mini=float('inf')
        while len(nums)>0:
            A_mini=min(nums)
            nums.remove(A_mini)
            B_mini=min(nums)
            nums.remove(B_mini)
            res.append(B_mini)
            res.append(A_mini)
        return res