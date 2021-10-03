# Task 1: Generalised Fibonacci
p = 1
q = 2
fibo =[1,1]

#fibo.append(fibo[0]+fibo[-1])
#print(fibo)
#fibo.append(fibo[0]+fibo[1]+fibo[2])
#print(fibo)


# Write your code here:

n=4
for i in range (2,n):
    fibo.append(fibo[i-2]+fibo[i-1])

print(fibo)

