class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit_S=0
        double_digit_S=0
        a= [0,1,2,3,4,5,6,7,8,9]
        for i in nums:
            if i in a:
                single_digit_S+=i
            else:
                double_digit_S+=i
        return  True if single_digit_S>double_digit_S or double_digit_S>single_digit_S else False


        