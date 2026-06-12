class solution:
    def number(self, n:int):
        m=0
        while(n>0):
            k=n%10
            if(k!=0 and n%k==0):
                m+=1
            n=n//10
        return m
obj=solution()
n=int(input("Enter number: "))
print(obj.number(n))