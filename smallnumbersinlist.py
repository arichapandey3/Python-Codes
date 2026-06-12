class solution:
    def count(self, n:list):
        m=[]
        for i in range(0,len(n)):
            count=0
            for j in range(0, len(n)):
                if(n[i]!=n[j]):
                   if(n[j]< n[i]):
                       count+=1
                   else:
                       count+=0
            m.append( count)
        return m
obj=solution()              
n=list(map(int, input("Enter the numbers separated by space: ").split()))
print(obj.count(n))