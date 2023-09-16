
def solve(nums):
   return sum([i for i in nums if i % 2 == 1])
nums=[]
n=int(input("enter no of numbers in list:"))
for i in range(n):
    a=eval(input("enter numbers:"))
    nums.append(a)
    print('lst=',nums)
    
print(solve(nums))
