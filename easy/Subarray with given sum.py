#Question: https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0
t=int(input())
for i in range(t):
    n,sum1=map(int,input().split())
    list1=list(map(int,input().split()))
    lb=0
    ub=0
    found=False
    for j in range(n):
        sum2=0
        for k in range(j,n):
            sum2=sum2+list1[k]
            if(sum2>sum1):
                break
            elif(sum2==sum1):
                lb=j+1
                ub=k+1
                found=True
                break
        if(found):
            break
    if(found):
        print(lb,end=" ")
        print(ub)
    else:
        print("-1")