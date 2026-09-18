class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxcount=0
        count=0
        for words in sentences:
            for char in words:
                if char==" ":
                    count+=1
            maxcount=max(count+1,maxcount)
            count=0
        return maxcount
        