#Question: https://practice.geeksforgeeks.org/problems/check-if-a-number-is-divisible-by-8/0
t=int(input())
for i in range(t):
    no=int(input())
    if(no%8==0):
        print(1)
    else:
        print(-1)