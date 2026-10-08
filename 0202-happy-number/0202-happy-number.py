class Solution:
    def sumOfSquares(self,n):
        s=0
        while n!=0:
            temp=n%10
            s+=(temp**2)
            n=n//10
        return s
    def isHappy(self, n: int) -> bool:
        f=n
        s=n
        while True:
            f=self.sumOfSquares(f)
            f=self.sumOfSquares(f)
            s=self.sumOfSquares(s)
            if f==s:
                break
        if f==1:
            return True
        else:
            return False