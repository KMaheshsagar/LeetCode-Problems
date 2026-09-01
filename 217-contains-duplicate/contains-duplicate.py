class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        re=set()
        for i in nums:
            if i not in re:
                re.add(i)
            else:
                return True
        return False


        