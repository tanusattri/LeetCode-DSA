class Solution:
    def sumAndMultiply(self, n: int) -> int:
        new= list()
        n= str(n)
        total=0
        for d in n:
            if d!='0':
                new.append(d)
        for i in new:
            total+=int(i)
        if len(new)==0:
            return 0
        return int("".join(new))*total