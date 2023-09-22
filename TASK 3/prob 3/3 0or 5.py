n=int(input("enter a num"))
total_sum=[]
for i in range(n):
    
    if i%3 == 0 or i%5 == 0:
        total_sum.append(i)
print(sum(total_sum))
        
