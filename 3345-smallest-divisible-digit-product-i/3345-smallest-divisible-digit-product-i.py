class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def productofDigits(num):
            product=1
            while num:
                product*=num%10
                num//=10
            return product
        while productofDigits(n)%t!=0:
            n+=1
        return n