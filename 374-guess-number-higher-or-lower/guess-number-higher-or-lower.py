# The guess API is already defined for you by the environment.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        
        while low <= high:
            mid = low + (high - low) // 2
            res = guess(mid)  # Call the predefined API
            
            if res == 0:
                return mid     # Correct guess
            elif res == -1:
                high = mid - 1 # The picked number is lower, search left
            else:
                low = mid + 1  # The picked number is higher, search right
                
        return -1
