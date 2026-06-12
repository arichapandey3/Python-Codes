class solution:
    def fibo(self,n:int):
        if n==0:
            return 0
        if n==1:
            return 1
        
        return(self.fibo(n - 1) + self.fibo(n - 2))
obj=solution()
n=int(input("Enter number: "))
for i in range(n):
    print(obj.fibo(i),end=" ")