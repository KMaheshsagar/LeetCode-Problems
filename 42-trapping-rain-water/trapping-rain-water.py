class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<3:
            return 0
        l=0
        r=len(height)-1
        leftmax=0
        rightmax=0
        trappedwater=0
         
        while l<=r:
            if height[l]<height[r]:
                if height[l]>leftmax:
                    leftmax=height[l]
                else:
                    trappedwater=trappedwater+leftmax-height[l]
                l+=1
            else:
                if height[r]>rightmax:
                    rightmax=height[r]
                else:
                    trappedwater=trappedwater+rightmax-height[r]
                r-=1
        return trappedwater
        