class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        arr=list(set(nums))
        j=0
        i=0
        while i<len(nums) and j<len(arr):
            if nums.count(arr[j])>(len(nums)//2):
                return arr[j]
            i+=1
            j+=1
        