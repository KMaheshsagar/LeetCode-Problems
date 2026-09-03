class Solution:
    def productExceptSelf(self, arr):
        n=len(arr)
        product=[1]*n
        p=1
        for i in range(n):
            product[i]=p
            p*=arr[i]
        p=1
        for i in range(n-1,-1,-1):
            product[i]*=p
            p*=arr[i]
        return product