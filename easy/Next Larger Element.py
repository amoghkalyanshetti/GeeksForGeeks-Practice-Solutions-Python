#Question:https://practice.geeksforgeeks.org/problems/next-larger-element/0
t=int(input())
for i in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    list2=[]
    for i in range(n):
        found=False
        for j in range(i+1,n):
            if(list1[j]>list1[i]):
                list2.append(list1[j])
                found=True
                break
        if(found==False):
            list2.append(-1)
    for var in list2:
        print(var,end=' ')
    print()