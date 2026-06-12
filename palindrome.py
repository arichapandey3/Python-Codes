class solution:
    def palindrome(self,n:int):
        num=0;
        temp=n
        while(temp>0):
            k=temp%10
            num=num*10+k
            temp=temp//10
        if num==n:
            print("The number is palindrome")
        else:       
            print("The number is not palindrome")  
obj=solution()
n=int(input("Enter number: "))  
obj.palindrome(n)