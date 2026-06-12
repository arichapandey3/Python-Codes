class solution:
    def fizzbuzz(self, n:int):
        m=[]
        for i in range(1, n+1):
            if(i%3==0 and i%5==0):
                m.append("fizzbuzz")
            elif(i%3==0):
                m.append("fizz")
            elif(i%5==0):
                m.append("buzz")
            else:
                m.append(str(i))
        return m
obj=solution()
m=int(input("Enter the number: "))
print(obj.fizzbuzz(m))