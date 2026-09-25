class Solution:
    def mergesort(self, left: list[int], right: list[int]) -> list[int]:
        l = 0
        r = 0
        nwlist = []
        
        # Merge elements in sorted order while both lists have elements
        while l < len(left) and r < len(right):
            if left[l] <= right[r]:
                nwlist.append(left[l])
                l += 1
            else:
                nwlist.append(right[r])
                r += 1
                
        # Append any remaining elements from left or right list
        nwlist.extend(left[l:])
        nwlist.extend(right[r:])
        
        return nwlist

    def sortArray(self, nums: list[int]) -> list[int]:
        # Base case: arrays with 0 or 1 element are already sorted
        if len(nums) <= 1:
            return nums
            
        mid = len(nums) // 2
        
        # Correct slicing to include all elements
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        # Return the merged result
        return self.mergesort(left, right)
