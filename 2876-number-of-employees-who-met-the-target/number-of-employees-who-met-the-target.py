class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        l=0
        r=len(hours)-1
        count=0
        while l<=r:
            if hours[l]>=target:
                count+=1
                l+=1
            elif hours[r]>=target:
                count+=1
                r-=1
            else:
                l+=1
                r-=1
        return count      