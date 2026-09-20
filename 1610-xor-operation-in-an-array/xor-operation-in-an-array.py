class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums=[]
        bitop=0
        for i in range(n):
            nums.append(start+2*i)
            bitop=bitop^nums[i]
        return bitop


        