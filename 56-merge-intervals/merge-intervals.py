class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n=len(intervals)
        intervals.sort()
        merge=[intervals[0]]
        
        for i in range(1,n):
            prevs=merge[-1]
            if intervals[i][0]<=prevs[1]:
                prevs[1]=max(intervals[i][1],prevs[1])
            else:
                merge.append(intervals[i])
        return merge
        