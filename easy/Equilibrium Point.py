#Question: https://practice.geeksforgeeks.org/problems/equilibrium-point/0
def calculate_equilibrium(list1):
    if(len(list1)==1):
        return 1
    sum1=0
    sum2=0
    n=len(list1)
    for i in range(1,n):
        sum1=0
        sum2=0
        for j in range(n):
            if(j<i):
                sum1+=list1[j]
            elif(j>i):
                sum2+=list1[j]
        if(sum1==sum2):
            return i+1
    return -1

#code
t=int(input())
for i in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    print(calculate_equilibrium(list1))