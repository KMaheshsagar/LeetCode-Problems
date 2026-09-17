class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(sentence)<26:
            return False
        alpha=[]
        for char in sentence:
            if char  not in alpha:
                alpha.append(char)
        return True if len(alpha)==26 else False
            
        