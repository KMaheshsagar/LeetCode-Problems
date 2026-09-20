class Solution:
    def countKeyChanges(self, s: str) -> int:
        cnginkey=0
        s_low=s.lower()
        for i in range(len(s_low)-1):
            if s_low[i]!=s_low[i+1]:
                cnginkey+=1
        return cnginkey