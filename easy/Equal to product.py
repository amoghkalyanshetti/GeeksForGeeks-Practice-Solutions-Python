#Question: https://practice.geeksforgeeks.org/problems/equal-to-product/0
t=int(input())
for i in range(t):
    n,product=map(int,input().split())
    productFound=False
    list1=list(map(int,input().split()))
    for j in range(len(list1)):
        for k in range(j+1,len(list1)):
            if(list1[j]*list1[k]==product):
                productFound=True
                break
        if(productFound):
            break
    if(productFound):
        print("Yes")
    else:
        print("No")