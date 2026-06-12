class solution:
    def odd(self, n:int,m:int):
        count=0
        for i in range(n,m+1):
            if(i%2!=0):
                count+=1
        return count
obj=solution()
n=int(input("Enter first: "))
m=int(input("Enter second:"))
print(obj.odd(n,m))