#Question: https://practice.geeksforgeeks.org/problems/leaders-in-an-array/0
t=int(input())
for k in range(t):
    n=int(input())
    list1=list(map(int,input().split()))
    list2=[]
    list3=[]
    for i in range(n):
        flag=False
        for j in range(i+1,n):
            if(list1[i]<list1[j]):
                flag=True
        if(flag==False):
            list2.append(list1[i])
            continue
    list3=list(set(list2))
    list3.sort(reverse=True)
    for var in list3:
        print(var,end=' ')
    print()